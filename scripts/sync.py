#!/usr/bin/env python3
"""
DIYSQ.com → GitHub 全景图自动同步脚本
从 WordPress REST API 拉取「360全景视觉」分类文章，增量同步到本仓库。

功能：
  - 分页拉取分类 ID=5 的全部文章
  - 按 modified 时间增量判断，只处理新增/变更条目
  - 从正文 <pre> 块提取并清洗 prompt JSON（处理网站的伪嵌套格式）
  - 下载特色图片并压缩为 2048px 宽 JPG
  - 生成标准 prompts/caseXXX.json
  - 重新生成 PROMPTS_LIST.md，更新 README 计数
  - 错误隔离：单篇失败不中断整体，记录到 sync_errors.log

用法：
  python scripts/sync.py              # 正常增量同步
  python scripts/sync.py --full       # 强制全量重新同步（忽略缓存时间）
  python scripts/sync.py --limit 10   # 只处理前 N 篇（调试用）
"""

import os
import re
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from datetime import datetime, timezone
from io import BytesIO

import requests
from PIL import Image

# ======================== 配置 ========================
WP_BASE = "https://www.diysq.com"
WP_API = f"{WP_BASE}/wp-json/wp/v2"
PANORAMA_CAT_ID = 5          # 360全景视觉分类 ID
PER_PAGE = 100
MAX_IMAGE_WIDTH = 2048       # 压缩后最大宽度
JPEG_QUALITY = 85
REQUEST_DELAY = 0.4          # API 请求间隔（秒），避免触发安全插件
REQUEST_TIMEOUT = 30
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# 路径（基于脚本位置定位仓库根目录）
REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
IMAGES_DIR = REPO_ROOT / "images"
CACHE_FILE = REPO_ROOT / ".data_cache.json"
PROMPTS_LIST_FILE = REPO_ROOT / "PROMPTS_LIST.md"
README_FILE = REPO_ROOT / "README.md"
ERROR_LOG = REPO_ROOT / "sync_errors.log"

# 分类 ID → 名称映射（运行时动态获取）
CAT_MAP: dict = {}

# ======================== 日志 ========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(ERROR_LOG, mode="w", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)


# ======================== API 层 ========================
def wp_get(endpoint: str, params: dict | None = None):
    """带重试和节流的 WP REST API GET 请求。"""
    url = f"{WP_API}/{endpoint}"
    headers = {"User-Agent": USER_AGENT}
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=REQUEST_TIMEOUT)
            if r.status_code == 200:
                time.sleep(REQUEST_DELAY)
                return r.json()
            if r.status_code == 403:
                log.error("403 Forbidden: %s (安全插件拦截 endpoint=%s)", url, endpoint)
                return None
            log.warning("HTTP %s for %s, attempt %s/3", r.status_code, url, attempt + 1)
        except requests.RequestException as e:
            log.warning("请求异常: %s, attempt %s/3", e, attempt + 1)
        time.sleep(2 * (attempt + 1))
    log.error("连续3次失败: %s", url)
    return None


def fetch_all_panoramas() -> list:
    """分页拉取 360全景分类下的全部文章，按修改时间倒序。"""
    all_posts = []
    page = 1
    while True:
        data = wp_get("posts", {
            "categories": PANORAMA_CAT_ID,
            "per_page": PER_PAGE,
            "page": page,
            "orderby": "modified",
            "order": "desc",
            "_fields": "id,date,modified,slug,title,content,categories,featured_media,link",
        })
        if data is None:
            log.error("第 %s 页拉取失败，停止", page)
            break
        if not isinstance(data, list) or not data:
            break
        all_posts.extend(data)
        log.info("第 %s 页: %s 篇，累计 %s 篇", page, len(data), len(all_posts))
        if len(data) < PER_PAGE:
            break
        page += 1
    return all_posts


def fetch_categories() -> dict:
    """获取分类 ID→名称 映射。"""
    global CAT_MAP
    data = wp_get("categories", {"per_page": 100, "_fields": "id,name,slug,parent"})
    if data:
        CAT_MAP = {c["id"]: c["name"] for c in data}
    return CAT_MAP


def fetch_image_url(media_id: int) -> str | None:
    """通过 media ID 获取又拍云原图 URL。"""
    if not media_id:
        return None
    media = wp_get(f"media/{media_id}", {"_fields": "source_url,media_details"})
    if not media:
        return None
    url = media.get("source_url")
    if url:
        return url
    # 回退：从 sizes 中取最大尺寸
    sizes = (media.get("media_details") or {}).get("sizes", {})
    for key in ("full", "diysq-hero", "large"):
        if key in sizes and sizes[key].get("source_url"):
            return sizes[key]["source_url"]
    return None


# ======================== Prompt 提取 ========================
def extract_prompt(content_html: str):
    """
    从文章正文 <pre> 块提取 prompt JSON。

    网站上的格式为「伪嵌套 JSON」：
        {
          "prompt": "{
          "全景空间锁定": { ... },
          ...
          "}
        }
    外层 {"prompt": "..."} 的内部引号未转义，无法直接 json.loads。
    处理方式：剥去外层包装，取中间的真实 JSON。

    返回: (prompt_dict, raw_pre_text)；失败返回 (None, raw_pre_text 或 None)
    """
    m = re.search(r"<pre[^>]*>(.*?)</pre>", content_html, re.DOTALL)
    if not m:
        # 回退：早期文章的 prompt 是纯文本，以"提示词"或"提示词简介"开头
        text = re.sub(r"<[^>]+>", " ", content_html)
        text = re.sub(r"\s+", " ", text).strip()
        for prefix in ("提示词简介", "提示词"):
            if text.startswith(prefix):
                prompt_text = text[len(prefix):].strip()
                # 取到下一个大标题前（如"核心视觉亮点解析"）
                idx = re.search(r"(核心视觉亮点|使用说明|参数|注意事项)", prompt_text)
                if idx:
                    prompt_text = prompt_text[:idx.start()].strip()
                if prompt_text:
                    return {"_raw_prompt": prompt_text[:5000]}, prompt_text
                break
        return None, None
    raw = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    if not raw:
        return None, None

    # 通用预处理：去掉各种包装前缀和标记
    cleaned = _clean_prompt_wrapper(raw)

    # 尝试直接解析清理后的文本
    try:
        obj = json.loads(cleaned)
        if isinstance(obj, dict):
            if "prompt" in obj and isinstance(obj["prompt"], str):
                inner_clean = _clean_prompt_wrapper(obj["prompt"])
                try:
                    return json.loads(inner_clean), raw
                except json.JSONDecodeError:
                    pass
            return obj, raw
    except json.JSONDecodeError:
        pass

    # 尝试自动修复
    fixed = _repair_json(cleaned)
    if fixed:
        try:
            return json.loads(fixed), raw
        except json.JSONDecodeError:
            pass

    log.warning("JSON 解析失败，保留原始文本")
    return {"_raw_prompt": cleaned[:5000]}, raw


def _clean_prompt_wrapper(text: str) -> str:
    """去掉 prompt 的各种包装前缀和标记，返回纯净的 JSON 文本。"""
    t = text.strip()

    # 第一步：剥掉外层 {"prompt": "..."} 伪嵌套包装
    # 匹配开头: { "prompt": " 或 { "prompt": （无值）— 只匹配行内空白，不跨行
    m = re.match(r'^\s*\{\s*"prompt"\s*:[ \t]*"?', t)
    if m:
        t = t[m.end():]
        # 匹配结尾: " } 或 }
        t = re.sub(r'"?\s*\}\s*$', "", t).strip()
        # 反转义
        t = t.replace('\\"', '"').replace("\\n", "\n").replace("\\\\", "\\")

    # 第二步：去掉所有 @创建图片 前缀（可能重复多次）
    while t.startswith("@创建图片"):
        t = t[len("@创建图片"):].strip()

    # 第三步：去掉 markdown 代码块标记（包括末尾带引号的情况）
    t = re.sub(r"^```(?:json)?\s*", "", t).strip()
    t = re.sub(r'\s*```"?\s*$', "", t).strip()

    # 第四步：去掉开头的多余引号（仅当去掉后以 { 或 [ 开头时）
    if t.startswith('"'):
        candidate = t[1:].lstrip()
        if candidate.startswith("{") or candidate.startswith("["):
            t = candidate.strip()

    # 第五步：去掉残留的 '"prompt":' 前缀
    t = re.sub(r'^\s*"prompt"\s*:\s*', "", t).strip()

    # 第六步：如果不以 { 或 [ 开头，补上外层 { }
    if t and not t.startswith("{") and not t.startswith("["):
        # 先平衡末尾括号
        while t.rstrip().endswith("}") and t.count("{") < t.count("}"):
            t = t.rstrip()[:-1].rstrip()
        t = "{\n" + t + "\n}"

    # 第七步：去掉末尾多余的引号
    t = re.sub(r'"\s*$', "", t).strip()

    # 第八步：转义字符串内的未转义换行符
    t = _escape_newlines_in_strings(t)

    return t


def _escape_newlines_in_strings(text: str) -> str:
    """将 JSON 字符串内部的裸换行符转义为 \\n。"""
    result = []
    in_string = False
    escape = False
    for c in text:
        if in_string:
            if escape:
                result.append(c)
                escape = False
            elif c == "\\":
                result.append(c)
                escape = True
            elif c == '"':
                result.append(c)
                in_string = False
            elif c == "\n":
                result.append("\\n")
            elif c == "\r":
                pass  # 忽略 \r
            else:
                result.append(c)
        else:
            if c == '"':
                in_string = True
            result.append(c)
    return "".join(result)


def _repair_json(text: str) -> str | None:
    """尝试修复常见的 JSON 语法错误（缺失逗号、多余逗号）。"""
    result = []
    i = 0
    n = len(text)
    in_string = False
    escape = False

    def prev_nonspace():
        j = len(result) - 1
        while j >= 0 and result[j] in " \t\n\r":
            j -= 1
        return result[j] if j >= 0 else ""

    while i < n:
        c = text[i]
        if in_string:
            result.append(c)
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            i += 1
            continue

        if c == '"':
            # 新字符串开始：前一个是值结束且不是冒号 → 补逗号
            prev = prev_nonspace()
            if prev in ('"', "}", "]") and prev != ":":
                # 检查前一个值结束是否是属性值（前面是冒号）
                j = len(result) - 1
                while j >= 0 and result[j] in " \t\n\r":
                    j -= 1
                # 向前找到冒号或逗号
                k = j
                while k >= 0 and result[k] not in ":,{[":
                    k -= 1
                if k >= 0 and result[k] != ":":
                    result.insert(j + 1, ",")
            in_string = True
            result.append(c)
            i += 1
            continue

        if c in " \t\n\r":
            result.append(c)
            i += 1
            continue

        if c in "{[":
            prev = prev_nonspace()
            if prev in ('"', "}", "]"):
                j = len(result) - 1
                while j >= 0 and result[j] in " \t\n\r":
                    j -= 1
                k = j
                while k >= 0 and result[k] not in ":,{[":
                    k -= 1
                if k >= 0 and result[k] != ":":
                    result.insert(j + 1, ",")

        if c in "}]":
            pass  # 对象/数组结束，不需要特殊处理

        result.append(c)
        i += 1

    fixed = "".join(result)
    # 去掉多余的 trailing comma
    fixed = re.sub(r",\s*}", "}", fixed)
    fixed = re.sub(r",\s*]", "]", fixed)
    return fixed


# ======================== 元数据推断 ========================
def get_primary_category(cat_ids: list) -> str:
    """从分类 ID 列表中选出最具体的分类名称（优先子分类）。"""
    names = [CAT_MAP[cid] for cid in cat_ids if cid in CAT_MAP]
    if not names:
        return "360全景视觉"
    for n in names:
        if n != "360全景视觉":
            return n
    return names[0]


def detect_model(prompt_dict: dict, title: str, categories: list) -> str:
    """根据分类、标题、prompt 内容推断 AI 模型。"""
    for cid in categories:
        cname = CAT_MAP.get(cid, "").lower()
        if "gpt" in cname:
            return "GPT Image"
    title_lower = title.lower()
    if any(k in title_lower for k in ("gpt", "chatgpt")):
        return "GPT Image"
    if "nano" in title_lower or "banana" in title_lower:
        return "Nano Banana"
    if "midjourney" in title_lower:
        return "Midjourney"
    if "flux" in title_lower:
        return "FLUX"
    prompt_str = json.dumps(prompt_dict, ensure_ascii=False).lower() if isinstance(prompt_dict, dict) else ""
    if "gpt" in prompt_str:
        return "GPT Image"
    return "GPT Image"


# ======================== 图片处理 ========================
def download_and_compress_image(image_url: str, dest_path: Path) -> bool:
    """下载图片，压缩为 2048px 宽 JPG，保存到 dest_path。"""
    headers = {"User-Agent": USER_AGENT, "Referer": WP_BASE + "/"}
    try:
        r = requests.get(image_url, headers=headers, timeout=60)
        if r.status_code != 200:
            log.error("图片下载失败 HTTP %s: %s", r.status_code, image_url[:80])
            return False
        img = Image.open(BytesIO(r.content))
        # 统一转 RGB（处理 PNG 透明通道）
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")
        # 等比缩放
        if img.width > MAX_IMAGE_WIDTH:
            ratio = MAX_IMAGE_WIDTH / img.width
            new_h = int(img.height * ratio)
            img = img.resize((MAX_IMAGE_WIDTH, new_h), Image.LANCZOS)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(dest_path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        return True
    except Exception as e:
        log.error("图片处理异常: %s -> %s", image_url[:80], e)
        return False


# ======================== 缓存 ========================
def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            log.warning(".data_cache.json 读取失败，将重建")
    return {}


def save_cache(cache: dict):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def get_next_case_id(cache: dict) -> str:
    """分配下一个 case_id（扫描缓存 + prompts 目录，取最大编号+1）。"""
    max_num = 0
    for item in cache.values():
        m = re.match(r"case(\d+)", str(item.get("case_id", "")))
        if m:
            max_num = max(max_num, int(m.group(1)))
    if PROMPTS_DIR.exists():
        for p in PROMPTS_DIR.glob("case*.json"):
            m = re.match(r"case(\d+)", p.stem)
            if m:
                max_num = max(max_num, int(m.group(1)))
    return f"case{max_num + 1:03d}"


# ======================== 产物生成 ========================
def clean_title(raw_title: str) -> str:
    """清洗网站文章标题，去掉营销前缀、后缀和 emoji，保留核心场景名。"""
    title = re.sub(r"<[^>]+>", "", raw_title).strip()
    # 去掉开头的常见营销前缀
    title = re.sub(
        r"^(AI绘画|AI生成|用AI生成|用AI创造|AI绘画\+提示词揭秘|一条提示词生成|AI生成的)\s*",
        "", title,
    )
    # 去掉 "360°全景图｜" / "360全景图：" / "360°全景｜" 等中间标记
    title = re.sub(r"^360[°度]?\s*全景图?\s*[｜|:：]\s*", "", title)
    # 去掉开头残留的 "｜" 或 ":"
    title = re.sub(r"^[｜|:：]\s*", "", title)
    # 去掉末尾的营销后缀（｜360°...、｜AI...、｜用AI...）
    title = re.sub(r"\s*[｜|]\s*(AI|360|用AI|一条提示词).*$", "", title)
    # 去掉 emoji 和特殊符号
    title = re.sub(
        r"[^\u4e00-\u9fff\u3000-\u303f\uff00-\uffef\w\s·\-—:：，。！？、()（）]",
        "", title,
    )
    return title.strip()


def generate_prompt_json(post: dict, case_id: str, prompt_dict: dict, image_rel: str) -> dict:
    """生成标准 prompts/caseXXX.json 内容。"""
    title = clean_title(post["title"]["rendered"])
    model = detect_model(prompt_dict, title, post.get("categories", []))
    category = get_primary_category(post.get("categories", []))
    return {
        "id": case_id,
        "website_id": post["id"],
        "title": title,
        "model": model,
        "style": "写实风格 / Photorealistic",
        "category": category,
        "constraints": ["equirectangular", "seamless", "360 panorama"],
        "website_url": post["link"],
        "image": image_rel,
        "prompt": prompt_dict,
        "website_published_at": post.get("date", ""),
        "website_updated_at": post.get("modified", ""),
        "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def generate_prompts_list(cache: dict):
    """重新生成 PROMPTS_LIST.md（合并缓存条目 + 手动添加的 prompts 文件）。"""
    items: dict[str, tuple[str, str]] = {}  # case_id -> (title, ext)

    # 来自缓存
    for item in cache.values():
        cid = str(item.get("case_id", ""))
        if cid:
            items[cid] = (item.get("title", cid), "")

    # 来自 prompts 目录扫描（补充无缓存的手动条目，如 case001-012）
    if PROMPTS_DIR.exists():
        for p in PROMPTS_DIR.glob("case*.json"):
            cid = p.stem
            if cid not in items:
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    title = data.get("title", cid)
                except (json.JSONDecodeError, OSError):
                    title = cid
                items[cid] = (title, "")

    # 确定图片扩展名
    for cid in list(items.keys()):
        title, _ = items[cid]
        img_base = IMAGES_DIR / cid
        ext = ".jpg"
        if (img_base / "output.png").exists():
            ext = ".png"
        elif (img_base / "output.jpg").exists():
            ext = ".jpg"
        elif (img_base / "output.jpeg").exists():
            ext = ".jpeg"
        items[cid] = (title, ext)

    sorted_items = sorted(items.items(), key=lambda x: x[0])
    lines = [
        "# 全部提示词列表 / Full Prompts List",
        "",
        f"共 {len(sorted_items)} 个提示词 / Total {len(sorted_items)} prompts",
        "",
        "| ID | 标题 | 提示词 JSON | 预览图片 |",
        "|:---|:---|:---|:---:|",
    ]
    for cid, (title, ext) in sorted_items:
        safe_title = title.replace("|", "\\|")[:60]
        lines.append(
            f"| {cid} | {safe_title} | [查看](prompts/{cid}.json) "
            f"| [预览](images/{cid}/output{ext}) |"
        )

    with open(PROMPTS_LIST_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    log.info("PROMPTS_LIST.md 已更新，共 %s 条", len(sorted_items))


def update_readme_count(count: int):
    """更新 README 中的提示词计数（badge + 标题中的数字）。"""
    if not README_FILE.exists():
        return
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    original = content
    # badge: Prompts-132+
    content = re.sub(
        r"(img\.shields\.io/badge/Prompts-)\d+(\+-)",
        rf"\g<1>{count}\g<2>",
        content,
    )
    # 中文标题: 🔥 132+ 全景提示词
    content = re.sub(
        r"(🔥\s*)\d+(\+\s*全景提示词)",
        rf"\g<1>{count}\g<2>",
        content,
    )
    # 英文: 132+ Panorama Prompts
    content = re.sub(
        r"(\b)\d+(\+\s*Panorama Prompts)",
        rf"\g<1>{count}\g<2>",
        content,
    )
    if content != original:
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        log.info("README 计数已更新为 %s", count)


# ======================== 主流程 ========================
def main():
    parser = argparse.ArgumentParser(description="DIYSQ → GitHub 全景图同步")
    parser.add_argument("--full", action="store_true", help="强制全量重新同步")
    parser.add_argument("--limit", type=int, default=0, help="只处理前 N 篇（调试用）")
    args = parser.parse_args()

    log.info("=" * 60)
    log.info("DIYSQ → GitHub 全景图同步开始 (full=%s, limit=%s)", args.full, args.limit)
    log.info("=" * 60)

    # 1. 分类映射
    fetch_categories()
    log.info("分类映射加载: %s 个分类", len(CAT_MAP))

    # 2. 拉取文章
    posts = fetch_all_panoramas()
    log.info("共拉取 %s 篇全景文章", len(posts))
    if not posts:
        log.error("未拉取到任何文章，终止")
        sys.exit(1)

    if args.limit > 0:
        posts = posts[:args.limit]
        log.info("调试模式：只处理前 %s 篇", args.limit)

    # 3. 加载缓存
    cache = load_cache()
    log.info("本地缓存: %s 条", len(cache))

    # 4. 增量同步
    new_count = update_count = skip_count = error_count = 0

    for idx, post in enumerate(posts, 1):
        wid = str(post["id"])
        modified = post.get("modified", "")
        title_short = re.sub(r"<[^>]+>", "", post["title"]["rendered"]).strip()[:40]

        # 判断是否需要处理
        cached = cache.get(wid)
        case_id = None
        needs_sync = True

        if cached and not args.full:
            case_id = cached.get("case_id")
            prompt_exists = case_id and (PROMPTS_DIR / f"{case_id}.json").exists()
            if cached.get("website_updated_at") == modified and prompt_exists:
                skip_count += 1
                needs_sync = False

        if not needs_sync:
            continue

        if not case_id:
            case_id = get_next_case_id(cache)
        action = "新增" if wid not in cache else "更新"
        log.info("[%s/%s][%s] %s → %s | %s", idx, len(posts), action, wid, case_id, title_short)

        # 4a. 提取 prompt
        prompt_dict, _ = extract_prompt(post["content"]["rendered"])
        if prompt_dict is None:
            log.error("  prompt 提取失败: article=%s", wid)
            error_count += 1
            continue

        # 4b. 获取图片 URL（可能没有特色图片）
        image_url = fetch_image_url(post.get("featured_media", 0))
        image_rel = ""
        if image_url:
            # 4c. 下载并压缩图片
            img_dest = IMAGES_DIR / case_id / "output.jpg"
            if not download_and_compress_image(image_url, img_dest):
                error_count += 1
                continue
            image_rel = f"images/{case_id}/output.jpg"
        else:
            log.info("  无特色图片，仅同步 prompt")

        # 4d. 生成 prompt JSON
        prompt_data = generate_prompt_json(post, case_id, prompt_dict, image_rel)
        prompt_path = PROMPTS_DIR / f"{case_id}.json"
        prompt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(prompt_path, "w", encoding="utf-8") as f:
            json.dump(prompt_data, f, ensure_ascii=False, indent=2)

        # 4e. 更新缓存
        cache[wid] = {
            "case_id": case_id,
            "title": prompt_data["title"],
            "model": prompt_data["model"],
            "category": prompt_data["category"],
            "image_url": image_url,
            "website_updated_at": modified,
            "website_published_at": post.get("date", ""),
            "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

        if wid not in cache or action == "新增":
            new_count += 1
        else:
            update_count += 1

        # 每 10 篇保存一次缓存（防中断）
        if (new_count + update_count) % 10 == 0:
            save_cache(cache)

    # 5. 保存最终缓存
    save_cache(cache)

    # 6. 生成文档
    total = len([v for v in cache.values() if v.get("case_id")])
    generate_prompts_list(cache)
    update_readme_count(total)

    # 7. 汇总
    log.info("=" * 60)
    log.info("同步完成: 新增 %s | 更新 %s | 跳过 %s | 失败 %s",
             new_count, update_count, skip_count, error_count)
    log.info("缓存条目总数: %s", len(cache))
    log.info("=" * 60)
    if error_count > 0:
        log.warning("有 %s 篇同步失败，详见 %s", error_count, ERROR_LOG)


if __name__ == "__main__":
    main()
