"""生成丰富版 README.md"""
import json
from pathlib import Path
from collections import defaultdict

REPO = Path(r"D:\开发\全景图库")
cache = json.load(open(REPO / ".data_cache.json", "r", encoding="utf-8"))

items = []
for wid, item in cache.items():
    cid = item.get("case_id")
    if not cid:
        continue
    img_path = REPO / "images" / cid / "output.jpg"
    items.append({
        "id": cid,
        "title": item.get("title", cid),
        "model": item.get("model", "GPT Image"),
        "category": item.get("category", "未分类"),
        "image": f"images/{cid}/output.jpg" if img_path.exists() else "",
        "updated": item.get("website_updated_at", "")[:10],
    })

# 按分类分组
by_cat = defaultdict(list)
for it in items:
    by_cat[it["category"]].append(it)

# 按数量排序分类
cats = sorted(by_cat.keys(), key=lambda c: len(by_cat[c]), reverse=True)

lines = []
lines.append("# 🌍 Awesome 360° Panorama Prompts")
lines.append("")
lines.append("> 最大的开源 360° 全景图提示词库 · 从 [DIYSQ.com](https://www.diysq.com) 自动同步")
lines.append("")
lines.append("[![在线预览](https://img.shields.io/badge/🌐_在线预览-点击交互浏览-2ea44f?style=for-the-badge)](https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/)")
lines.append("")
lines.append(f"本仓库收录 **{len(items)}** 条 360° 全景图提示词，每条包含完整的结构化 JSON，可直接用于 GPT Image 等模型生成无缝拼接的等距柱状投影（Equirectangular）全景图。")
lines.append("")
lines.append("## ✨ 特性")
lines.append("")
lines.append("- 🤖 **GPT Image 兼容** — 结构化 JSON 格式，直接粘贴即可生成")
lines.append("- 🥽 **VR Ready** — 标准 2:1 等距柱状投影，支持 Pannellum / Krpano")
lines.append("- 📄 **JSON Format** — 全景规范、场景描述、光影氛围、材质细节、负面约束")
lines.append("- 🔄 **自动同步** — GitHub Actions 每天自动从 diysq.com 拉取最新内容")
lines.append("- 🖼️ **预览图** — 每条提示词附带生成效果预览")
lines.append("")
lines.append("## 📂 目录结构")
lines.append("")
lines.append("```")
lines.append("├── prompts/          # 提示词 JSON 文件")
lines.append("├── images/           # 预览图")
lines.append("├── scripts/sync.py   # 同步脚本")
lines.append("├── .github/workflows # 自动同步工作流")
lines.append("└── index.html        # 在线演示页")
lines.append("```")
lines.append("")
lines.append("## 🖼️ 全部提示词")
lines.append("")

# 分类导航
lines.append("**分类导航：** " + " · ".join([f"[{c} ({len(by_cat[c])})](#{c.lower().replace(' ','-')})" for c in cats]))
lines.append("")

for cat in cats:
    cat_items = by_cat[cat]
    lines.append(f"### {cat} ({len(cat_items)} 个)")
    lines.append("")
    lines.append("| 预览 | 标题 | 模型 | 更新时间 | Prompt |")
    lines.append("|------|------|------|----------|--------|")
    for it in sorted(cat_items, key=lambda x: x["id"]):
        img = f"![{it['id']}]({it['image']})" if it["image"] else "无图"
        title = it["title"][:50] + ("..." if len(it["title"]) > 50 else "")
        lines.append(f"| {img} | {title} | {it['model']} | {it['updated']} | [JSON](prompts/{it['id']}.json) |")
    lines.append("")

lines.append("## 🔄 自动同步机制")
lines.append("")
lines.append("GitHub Actions 每天北京时间 8:00 自动运行：")
lines.append("")
lines.append("- 通过 WordPress REST API 拉取 diysq.com 全景分类文章")
lines.append("- 对比缓存，仅同步新发布或更新的内容（增量同步）")
lines.append("- 自动压缩预览图至 2048px JPEG")
lines.append("- 提交并推送到本仓库")
lines.append("")
lines.append("手动触发：仓库 → Actions → Sync from DIYSQ → Run workflow")
lines.append("")
lines.append("## 📄 License")
lines.append("")
lines.append("MIT")

readme = "\n".join(lines)
with open(REPO / "README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"README 已生成: {len(items)} 条提示词，{len(cats)} 个分类")
