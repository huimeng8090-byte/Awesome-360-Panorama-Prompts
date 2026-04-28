# 🌐 Awesome 360° Panorama Prompts

<div align="center">

**English** | [中文](README.md)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Website](https://img.shields.io/badge/Website-diysq.com-blue)](https://www.diysq.com)

**A curated collection of GPT Image 2.0 prompts for 360° Equirectangular Panorama generation**

> All prompts use a structured JSON format, covering indoor spaces, natural landscapes, tropical resorts, and more. Each prompt can be directly used with GPT Image 2.0.

</div>

---

## 🍌 Introduction

This repository collects **GPT Image 2.0** prompts for generating 360° equirectangular panoramic images, curated from **[HuiMengShiGuang (绘梦拾光)](https://www.diysq.com)**.

Each prompt follows a standardized JSON schema containing:
- `Image Metadata`: Projection type, aspect ratio (must be 2:1), resolution
- `Scene Composition`: Location, camera position/height, weather, depth of field
- `Visual Elements`: Foreground, midground, background, atmosphere
- `Render Style`: Lighting, color grading, texture quality
- `Constraints`: Must-keep / Must-avoid items
- `Negative Prompts`: Exclusion list

---

## 📰 How to Use

1. Browse the examples below and find your desired scene
2. Copy the entire JSON from the **Prompt** code block
3. Paste it directly into **GPT Image 2.0** (ChatGPT image generation)
4. Output will be in **2:1 aspect ratio**, ready for 360° panorama viewers

> [!NOTE]
> All prompts are optimized for **Equirectangular Projection**. The generated images can be loaded directly into VR panorama viewers or tools like Pannellum.

---

## 📑 Contents

- [🏠 Indoor Spaces](#-indoor-spaces)
  - [Case 1: Luxury Arc Dining Room](#case-1-luxury-arc-dining-room)
  - [Case 2: Immersive Modern Concert Hall](#case-2-immersive-modern-concert-hall)
- [🌊 Tropical Resort](#-tropical-resort)
  - [Case 3: Tropical Island Luxury Resort](#case-3-tropical-island-luxury-resort)
  - [Case 4: Island Bungalow Interior View](#case-4-island-bungalow-interior-view)
  - [Case 5: Tropical Island Sunset Coconut Grove](#case-5-tropical-island-sunset-coconut-grove)
  - [Case 6: Sunset Sailing on Open Sea](#case-6-sunset-sailing-on-open-sea)
- [🐠 Ocean Nature](#-ocean-nature)
  - [Case 7: Manta Ray Half-Water Panorama](#case-7-manta-ray-half-water-panorama)
  - [Case 8: Terraced Reef Atoll Panorama](#case-8-terraced-reef-atoll-panorama)
  - [Case 9: High-Altitude Coral Atoll Panorama](#case-9-high-altitude-coral-atoll-panorama)

---

## 🏠 Indoor Spaces

### Case 1: Luxury Arc Dining Room

| Output |
| :---: |
| <img src="images/case01/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "现代轻奢风格环形餐厅与开放式厨房融合空间",
    "相机位置": "餐厅中央圆形餐桌上方略偏心位置",
    "相机高度": "约1.6米人眼高度",
    "视野范围": "水平360度，垂直180度",
    "投影行为": "正确的等距柱状畸变，确保无缝球形拼接",
    "天气状况": "晴朗午后，自然光充足",
    "景深": "全景清晰，远近细节均锐利"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "大理石圆形餐桌，搭配皮革与藤编混合餐椅，桌面摆放水果与精致餐具",
      "动态": "轻微窗帘飘动与自然光影变化"
    },
    "中景主体": {
      "地形": "暖色调石材拼接地面与弧形木饰面结构",
      "区域": "开放式厨房岛台、壁炉式烤炉与展示酒架融合",
      "云雾": "无云雾，强调通透空间感"
    },
    "背景": {
      "景观": "弧形落地窗与休闲沙发区、壁龛展示架",
      "天空": "柔和蓝天透过窗户进入室内"
    },
    "环境氛围": {
      "地面半球": "自然材质交错，纹理细腻真实",
      "整体氛围": "温暖、优雅、静谧的高端居家用餐环境"
    }
  },
  "渲染风格": {
    "光照": "自然光与柔和吊灯混合照明，强调顶部雕花细节与材质层次",
    "调色": "米白、暖木色与浅金色点缀的高级配色",
    "质感质量": {
      "描述": "超写实材质表现，大理石纹理、木饰面与金属细节真实细腻",
      "痕迹": "无人工痕迹，画面纯净，自然锐化",
      "拼接": "完美的360度无缝拼接"
    },
    "全景约束强化": {
      "边界连续性": "图像最左边与最右边必须完全无缝拼接，结构连续一致",
      "空间结构": "室内为环形开放结构，所有家具围绕中心分布",
      "禁止断层": "禁止出现左右结构不一致或空间跳跃"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "室内环形空间结构", "高端餐厅氛围", "无任何界面元素", "高度写实摄影感"],
    "必须避免": ["人物", "过度戏剧化灯光", "奇幻风格", "插画或绘画质感", "非全景构图", "结构拼接错误"]
  },
  "负面提示词": ["用户界面", "抬头显示", "文本覆盖", "水印", "人物", "卡通风格", "低分辨率", "过曝", "噪点", "边框", "裁剪视图", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5626](https://www.diysq.com/archives/5626)

---

### Case 2: Immersive Modern Concert Hall

| Output |
| :---: |
| <img src="images/case02/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "16K超高清全景"
  },
  "场景构图": {
    "地点": "未来感大型交响音乐厅内部（原创设计，非现实复刻）",
    "相机位置": "舞台中央略偏后位置",
    "相机高度": "约1.6米人眼视角",
    "视野范围": "水平360度，垂直180度",
    "投影行为": "精准等距柱状投影，边缘无拉裂，结构连续",
    "天气状况": "室内恒定光环境，无自然天气干扰",
    "景深": "全景深清晰，前中后景均锐利"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "圆形指挥台与木质舞台地板，带细腻纹理反射",
      "动态": "无人物但暗示演出前静谧氛围"
    },
    "中景主体": {
      "地形": "环形阶梯式观众席层层上升，结构流畅"
    },
    "背景": {
      "景观": "弧形包裹式声学墙面与悬浮式阳台结构",
      "天空": "穹顶式天花板，嵌入点状暖光灯阵列"
    },
    "环境氛围": {
      "整体氛围": "安静、庄重、具有未来感与艺术气息"
    }
  },
  "渲染风格": {
    "光照": "柔和暖色顶灯+隐藏式间接光源，均匀照明无死角",
    "调色": "暖棕木色+深灰结构+柔金灯光对比",
    "全景约束强化": {
      "边界连续性": "左右边界完全对齐，座椅与墙体连续闭合",
      "空间结构": "环形开放式音乐厅，观众席围绕中心舞台"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "中心舞台结构", "环形观众席布局", "无人物环境", "高度写实摄影风格"],
    "必须避免": ["真实地标音乐厅复刻", "人物或演员", "强烈戏剧光影", "奇幻或科幻过度风格", "插画或CG感过重"]
  },
  "负面提示词": ["水印", "UI界面", "文字", "观众", "演员", "摄影机", "畸形透视", "接缝断裂", "模糊", "过曝", "低分辨率"]
}
```

> Source: [diysq.com/archives/5619](https://www.diysq.com/archives/5619)

---

## 🌊 Tropical Resort

### Case 3: Tropical Island Luxury Resort

| Output |
| :---: |
| <img src="images/case04/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "16K超高清全景分辨率"
  },
  "场景构图": {
    "地点": "热带印度洋环礁私人岛屿",
    "相机位置": "岛屿正中心上空垂直俯视略倾斜角度",
    "相机高度": "约120米无人机航拍高度",
    "视野范围": "水平360度，垂直180度",
    "投影行为": "严格等距柱状投影，海岸线与栈桥在左右边界无缝衔接",
    "天气状况": "晴朗蓝天，低密度积云，能见度极高",
    "景深": "超深景深，从浅海礁石到远海地平线全部清晰"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "环形白色沙滩与浅turquoise色泻湖，清晰可见珊瑚礁纹理",
      "动态": "海水轻微波纹，阳光反射形成闪烁高光"
    },
    "中景主体": {
      "地形": "被浓密棕榈树林覆盖的椭圆形岛屿",
      "区域": "岛一侧延伸出弧形水上别墅木栈桥，整齐排列的水屋"
    },
    "背景": {
      "景观": "深蓝色开阔海洋延伸至地平线，形成明显色阶过渡",
      "天空": "渐变蓝天空，点缀柔软积云，空间层次丰富"
    },
    "环境氛围": {
      "整体氛围": "宁静、奢华、度假感强烈，带有纯净自然的沉浸体验"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "无人机高空视角", "热带海岛与水上别墅为核心主体", "无任何界面元素", "高度写实摄影感"],
    "必须避免": ["城市或高楼建筑", "人物或船只特写", "电影感夸张光效", "奇幻或游戏风格", "绘画或插画感"]
  },
  "负面提示词": ["用户界面", "文本覆盖", "水印", "现代城市", "人物", "奇幻艺术", "插图风格", "过度HDR", "边框", "拼接错误"]
}
```

> Source: [diysq.com/archives/5587](https://www.diysq.com/archives/5587)

---

### Case 4: Island Bungalow Interior View

| Output |
| :---: |
| <img src="images/case05/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "热带海岛私人沙滩度假木屋",
    "相机位置": "室内木屋中央，正对开放式落地推拉门",
    "相机高度": "约1.4米人眼视角",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗蓝天，轻微海风，阳光明亮"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "木质地板、拖鞋、毛巾、简约木制家具、室内柔和阴影"
    },
    "中景主体": {
      "地形": "洁白细腻沙滩，几棵倾斜的椰子树",
      "区域": "简易茅草遮阳亭与躺椅"
    },
    "背景": {
      "景观": "清澈渐变蓝色海水与平直海平线",
      "天空": "高饱和蓝天，零星白云"
    },
    "环境氛围": {
      "整体氛围": "宁静、度假感强、温暖舒适、开放通透"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "室内外一体化构图", "海滩与椰树为核心主体", "高度写实摄影感"],
    "必须避免": ["城市或现代建筑", "人物", "奇幻或游戏风格", "绘画或插画感"]
  },
  "负面提示词": ["水印", "现代建筑", "行人", "奇幻艺术", "插图", "边框", "裁剪视图", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5582](https://www.diysq.com/archives/5582)

---

### Case 5: Tropical Island Sunset Coconut Grove

| Output |
| :---: |
| <img src="images/case07/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "热带海岛椰林海滩，临海浅水区域，远处有水上屋与栈桥",
    "相机位置": "无人机悬停于海滩与浅海交界上方中心点",
    "相机高度": "约15-25米低空俯视",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗傍晚，夕阳接近地平线，少量薄云"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "细腻白色沙滩与浅海水面，轻微水纹与倒影"
    },
    "背景": {
      "景观": "广阔海面延伸至地平线，岛屿轮廓隐约可见",
      "天空": "夕阳橙红渐变至紫蓝色天空，色彩自然过渡"
    },
    "环境氛围": {
      "整体氛围": "宁静、温暖、真实的热带海岛落日氛围"
    }
  },
  "渲染风格": {
    "光照": "真实自然夕阳逆光，长阴影与柔和高光",
    "调色": "暖橙与冷蓝渐变平衡，低饱和高真实感"
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "无人机高空视角", "热带椰林与海滩为核心主体", "高度写实摄影感"],
    "必须避免": ["城市或现代建筑", "人物", "奇幻或游戏风格"]
  },
  "负面提示词": ["水印", "现代建筑", "行人", "奇幻艺术", "插图", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5571](https://www.diysq.com/archives/5571)

---

### Case 6: Sunset Sailing on Open Sea

| Output |
| :---: |
| <img src="images/case10/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "原始自然海岸与梯田交融地貌",
    "相机位置": "无人机悬停于海岸线与梯田交界上空",
    "相机高度": "距地面约120米高空",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗傍晚，低空云层稀疏，夕阳明显"
  },
  "视觉元素": {
    "背景": {
      "景观": "辽阔海面延展至地平线，一艘帆船形成剪影",
      "天空": "橙红渐变至深蓝的日落天空，太阳接近海平线"
    },
    "环境氛围": {
      "整体氛围": "宁静、温暖、广阔、真实摄影质感"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "无人机高空视角", "梯田与帆船为核心主体", "高度写实摄影感"],
    "必须避免": ["城市或现代建筑", "人物", "奇幻或游戏风格"]
  },
  "负面提示词": ["水印", "现代建筑", "行人", "奇幻艺术", "边框", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5554](https://www.diysq.com/archives/5554)

---

## 🐠 Ocean Nature

### Case 7: Manta Ray Half-Water Panorama

| Output |
| :---: |
| <img src="images/case06/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "热带浅海海域与水上度假区",
    "相机位置": "水面交界处（半水半空）",
    "相机高度": "略高于水面中心线",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗天空，少量白云"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "水下沙地与两只清晰可见的魔鬼鱼",
      "动态": "魔鬼鱼缓慢滑行，尾部轻微摆动"
    },
    "背景": {
      "景观": "延伸的海平线与远处岛屿轮廓",
      "天空": "高饱和蓝天与自然云层"
    },
    "环境氛围": {
      "整体氛围": "宁静、通透、真实自然的热带海洋环境"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "半水面双世界结构", "魔鬼鱼为核心主体", "高度写实摄影感"],
    "必须避免": ["城市高楼或现代密集建筑", "人物主体", "奇幻或游戏风格"]
  },
  "负面提示词": ["水印", "现代高楼", "行人", "奇幻艺术", "边框", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5576](https://www.diysq.com/archives/5576)

---

### Case 8: Terraced Reef Atoll Panorama

| Output |
| :---: |
| <img src="images/case08/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "热带海洋环礁与梯田状海底地貌融合区域",
    "相机位置": "无人机悬停于环礁中心上空",
    "相机高度": "距海平面约300米",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗少云，远处有体积感积云"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "环礁边缘的白色沙洲与浅水梯田状纹理"
    },
    "中景主体": {
      "地形": "层层递进的梯田式海底地貌与珊瑚礁结构"
    },
    "背景": {
      "景观": "无边际深蓝海洋逐渐过渡至地平线",
      "天空": "高空蓝天与立体白云分布均匀"
    },
    "环境氛围": {
      "整体氛围": "宁静、纯净、真实的自然生态环境"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "无人机高空视角", "梯田为核心主体", "高度写实摄影感"],
    "必须避免": ["城市或现代建筑", "人物", "奇幻或游戏风格"]
  },
  "负面提示词": ["水印", "现代建筑", "行人", "奇幻艺术", "边框", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5565](https://www.diysq.com/archives/5565)

---

### Case 9: High-Altitude Coral Atoll Panorama

| Output |
| :---: |
| <img src="images/case09/output.png" width="600"> |

**Prompt:**

```json
{
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "宽高比": "2:1",
    "分辨率": "超高分辨率全景"
  },
  "场景构图": {
    "地点": "热带海域环形珊瑚礁与潟湖",
    "相机位置": "无人机悬停于环礁正上方中心略偏外侧",
    "相机高度": "约1500米高空俯视",
    "视野范围": "水平360度，垂直180度",
    "天气状况": "晴朗蓝天，零散积云漂浮"
  },
  "视觉元素": {
    "前景": {
      "主体视图": "清澈蔚蓝海面与浅绿渐变的珊瑚礁边缘"
    },
    "中景主体": {
      "地形": "完整环形珊瑚礁围绕深蓝潟湖，色彩由浅至深渐变"
    },
    "背景": {
      "景观": "无边际深蓝海洋延伸至地平线",
      "天空": "高空通透蓝天与层次丰富的云团"
    },
    "环境氛围": {
      "整体氛围": "宁静、纯净、广阔、自然奇观感"
    }
  },
  "约束条件": {
    "必须保留": ["纯360度全景透视", "无人机高空视角", "环形珊瑚礁为核心主体", "高度写实摄影感"],
    "必须避免": ["城市或现代建筑", "人物", "奇幻或游戏风格"]
  },
  "负面提示词": ["水印", "现代建筑", "行人", "奇幻艺术", "边框", "全景接缝断裂"]
}
```

> Source: [diysq.com/archives/5560](https://www.diysq.com/archives/5560)

---

## 🔗 Links

- 🌐 **Website**: [diysq.com](https://www.diysq.com)
- 📂 **360° Category**: [diysq.com/archives/category/360quanjing](https://www.diysq.com/archives/category/360quanjing)
- 🍌 **Inspired by**: [PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images)

## 📄 License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — Attribution required.
