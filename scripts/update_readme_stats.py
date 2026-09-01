"""自动更新 README.md 中的分类统计徽章"""
import json
import re
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

# 生成徽章 HTML
badges = []
for i, (cat, count) in enumerate(cats):
    color = colors[i % len(colors)]
    cat_escaped = cat.replace(" ", "_")
    badges.append(f'<img src="https://img.shields.io/badge/{cat_escaped}-{count}-{color}?style=flat-square">')

badges_html = '<p align="center">\n' + "\n".join(badges) + "\n</p>"

# 读取 README
readme_path = REPO / "README.md"
readme = readme_path.read_text(encoding="utf-8")

# 替换分类统计部分（从 ## 📊 分类统计 到下一个 ## 之前）
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

readme_path.write_text(new_readme, encoding="utf-8")
print(f"README 统计已更新: 共 {total} 条, {len(cats)} 个分类")
for cat, count in cats:
    print(f"  {cat}: {count}")
