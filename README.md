# 🌍 Awesome 360° Panorama Prompts

> 最大的开源 360° 全景图提示词库 · 从 [DIYSQ.com](https://www.diysq.com) 自动同步

本仓库收录 445+ 条 360° 全景图提示词，每条包含完整的结构化 JSON，可直接用于 GPT Image 等模型生成无缝拼接的等距柱状投影（Equirectangular）全景图。

## ✨ 特性

- 🤖 **GPT Image 兼容** — 结构化 JSON 格式，直接粘贴即可生成
- 🥽 **VR Ready** — 标准 2:1 等距柱状投影，支持 Pannellum / Krpano 等全景播放器
- 📄 **JSON Format** — 每条提示词包含全景规范、场景描述、光影氛围、材质细节、负面约束等完整字段
- 🔄 **自动同步** — GitHub Actions 每天自动从 diysq.com 拉取最新全景图
- 🖼️ **预览图** — 每条提示词附带生成效果预览

## 📁 目录结构

```
├── prompts/          # 提示词 JSON 文件（case013.json 起）
├── images/           # 预览图（每条一个目录，含 output.jpg）
├── scripts/sync.py   # 同步脚本
├── .github/workflows/sync.yml  # 自动同步工作流
├── PROMPTS_LIST.md   # 提示词索引表
└── demo.html         # 在线浏览演示页
```

## 🚀 快速开始

1. 按分类浏览，选择接近目标场景的案例
2. 点击「查看 Prompt」复制完整 JSON
3. 调整场景变量（如地点、时间、天气），生成你的全景图
4. 导入 Pannellum / Krpano 验证无缝拼接

## 🔄 自动同步机制

GitHub Actions 每天北京时间 8:00 自动运行：
- 通过 WordPress REST API 拉取 diysq.com 全景分类文章
- 对比缓存，仅同步新发布或更新的内容（增量同步）
- 自动压缩预览图至 2048px JPEG
- 提交并推送到本仓库

手动触发：仓库 → Actions → Sync from DIYSQ → Run workflow

## 📊 统计

- **445** 条全景提示词
- **444** 张预览图
- **16** 个分类

## 📝 分类

360全景视觉、GPT Image 2.0、景区、街头、客厅、人物、插画、花、游戏场景、科幻场景、古建筑、动物、建筑、瀑布、酒店、海底世界

## 📄 License

MIT
