"""自动更新 README.md 中的分类统计徽章"""
import json
import re
import urllib.parse
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).parent.parent
cache = json.load(open(REPO / ".data_cache.json", "r", encoding="utf-8"))

# 统计各分类数量
by_cat = defaultdict(int)
for wid, item in cache.items():
    cat = item.get("category", "未分类")
    by_cat[cat] += 1

# 按数量降序排列
cats = sorted(by_cat.items(), key=lambda x: x[1], reverse=True)

# 颜色循环
colors = ["0969da", "1a7f37", "8250df", "f778ba", "d2992c"]

# 生成徽章 HTML（带跳转链接）
badges = []
for i, (cat, count) in enumerate(cats):
    color = colors[i % len(colors)]
    cat_escaped = cat.replace(" ", "_")
    cat_url = urllib.parse.quote(cat)
    link = f"https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/?category={cat_url}"
    badges.append(f'<a href="{link}" target="_blank"><img src="https://img.shields.io/badge/{cat_escaped}-{count}-{color}?style=flat-square"></a>')

badges_html = '<p align="center">\n' + "\n".join(badges) + "\n</p>"

# 读取 README
readme_path = REPO / "README.md"
readme = readme_path.read_text(encoding="utf-8")

# 用更可靠的方式替换分类统计部分
# 找到 ## 📊 分类统计 和 下一个 ## 标题之间的内容
start_marker = "## 📊 分类统计"
end_marker = "## 🔄 自动同步机制"

start_idx = readme.find(start_marker)
end_idx = readme.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # 保留开头标记，替换中间内容，保留结尾标记
    before = readme[:start_idx + len(start_marker)]
    after = readme[end_idx:]
    new_readme = before + "\n\n" + badges_html + "\n\n" + after
else:
    print("警告：未找到分类统计部分，正则替换")
    pattern = r'(## 📊 分类统计\n\n).*?(\n## )'
    replacement = r'\1' + badges_html + r'\2'
    new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

# 同时更新顶部的提示词总数徽章
total = len(cache)
new_readme = re.sub(
    r'(<img src="https://img\.shields\.io/badge/提示词-)\d+(\+?-8250df\?style=flat-square">)',
    rf'\g<1>{total}\g<2>',
    new_readme
)

# 更新描述文字里的数字
new_readme = re.sub(
    r'(本仓库收录\s*\**)\d+(\+\**\s*条)',
    rf'\g<1>{total}\g<2>',
    new_readme
)

# 更新"查看全部 XXX 条"链接里的数字
new_readme = re.sub(
    r'(查看全部\s*)\d+(\s*条)',
    rf'\g<1>{total}\g<2>',
    new_readme
)

readme_path.write_text(new_readme, encoding="utf-8")
print(f"README 统计已更新: 共 {total} 条, {len(cats)} 个分类")
for cat, count in cats:
    print(f"  {cat}: {count}")
