# 🌍 Awesome 360° Panorama Prompts

> 最大的开源 360° 全景图提示词库 · 从 <a href="https://www.diysq.com" target="_blank">DIYSQ.com</a> 自动同步

<p align="center">
  <a href="https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/" target="_blank">
    <img src="https://img.shields.io/badge/🌐_在线预览-点击浏览全部提示词-2ea44f?style=for-the-badge" width="450">
  </a>
</p>

<p align="center">
  <a href="https://www.diysq.com/" target="_blank"><img src="https://img.shields.io/badge/🌐_官网-diysq.com-0969da"></a>
  <a href="https://www.diysq.com/ai360/" target="_blank"><img src="https://img.shields.io/badge/🎨_绘图站-AI360全景-1a7f37"></a>
  <img src="https://img.shields.io/badge/提示词-445+-8250df">
  <img src="https://img.shields.io/badge/分类-16-f778ba">
</p>

本仓库收录 **445+** 条 360° 全景图提示词，每条包含完整的结构化 JSON，可直接用于 GPT Image 等模型生成无缝拼接的等距柱状投影（Equirectangular）全景图。

## ✨ 特性

- 🤖 **GPT Image 兼容** — 结构化 JSON 格式，直接粘贴即可生成
- 🥽 **VR Ready** — 标准 2:1 等距柱状投影，支持 Pannellum / Krpano 等全景播放器
- 📄 **JSON Format** — 全景规范、场景描述、光影氛围、材质细节、负面约束等完整字段
- 🔄 **自动同步** — GitHub Actions 每天自动从 diysq.com 拉取最新全景图
- 🖼️ **预览图** — 每条提示词附带生成效果预览
- 🔍 **在线浏览** — 支持搜索、分类筛选、卡片/列表双视图

## 🖼️ 预览

|  |  |  |
|---|---|---|
| ![case033](images/case033/output.jpg) | ![case299](images/case299/output.jpg) | ![case300](images/case300/output.jpg) |
| ![case301](images/case301/output.jpg) | ![case302](images/case302/output.jpg) | ![case303](images/case303/output.jpg) |

<p align="center"><a href="https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/" target="_blank">→ 查看全部 445 条</a></p>

## 📁 目录结构

```
├── prompts/              # 提示词 JSON 文件（case013.json 起）
├── images/               # 预览图（每条一个目录，含 output.jpg）
├── scripts/sync.py       # 同步脚本
├── .github/workflows/    # 自动同步工作流
├── index.html            # 在线演示页
├── PROMPTS_LIST.md       # 提示词索引表
└── README.md
```

## 🚀 快速开始

1. 访问 <a href="https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/" target="_blank">在线演示页</a>
2. 按分类浏览或搜索目标场景
3. 点击「查看 Prompt」复制完整 JSON
4. 粘贴到 GPT Image 等模型，调整场景变量生成全景图
5. 导入 Pannellum / Krpano 验证无缝拼接

## 📊 分类统计

| 分类 | 数量 | 分类 | 数量 |
|---|---|---|---|
| 360全景视觉 | 159 | 插画 | 14 |
| GPT Image 2.0 | 87 | 花 | 10 |
| 景区 | 75 | 游戏场景 | 7 |
| 街头 | 25 | 科幻场景 | 7 |
| 客厅 | 23 | 古建筑 | 6 |
| 人物 | 15 | 动物 | 4 |
| 建筑 | 4 | 瀑布 | 4 |
| 酒店 | 3 | 海底世界 | 2 |

## 🔄 自动同步机制

GitHub Actions 每天北京时间 8:00 自动运行：

- 通过 WordPress REST API 拉取 diysq.com 全景分类文章
- 对比缓存，仅同步新发布或更新的内容（增量同步）
- 自动压缩预览图至 2048px JPEG
- 提交并推送到本仓库

**手动触发**：仓库 → Actions → Sync from DIYSQ → Run workflow

## 📝 提示词格式示例

```json
{
  "全景规范": {
    "图片类型": "360度等距长方全景图",
    "画幅比例": "2:1",
    "投影方式": "完整球形柱状投影"
  },
  "场景描述": "...",
  "光影氛围": "...",
  "材质细节": "...",
  "负面约束": [...]
}
```

## 📄 License

MIT
