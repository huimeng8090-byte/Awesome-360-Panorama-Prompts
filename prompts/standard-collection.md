# 🌐 Standard Prompt Collection — 精选全景提示词标准集

> **格式说明 Format Notes**
> - 所有提示词均采用 JSON 结构化格式，包含完整相机参数、场景构图和渲染规范
> - 所有案例强制包含 `--ar 2:1` 和 `equirectangular 360 degree panorama` 关键参数
> - All prompts use JSON structured format with full camera specs, scene composition, and rendering guidelines
> - All cases mandatorily include `--ar 2:1` and `equirectangular 360 degree panorama` parameters

---

## Case S-001 · 赛博朋克城市夜景 Cyberpunk City Night

**场景标签 Tags:** `cyberpunk` `city` `night` `neon` `volumetric lighting` `urban` `sci-fi`

**一句话描述:** 雨后霓虹赛博朋克大都市，容积光穿透水雾，360° 沉浸式科幻体验

**One-liner:** Rain-soaked cyberpunk megacity, volumetric neon light cutting through vapor, 360° immersive sci-fi experience

### 📋 JSON 提示词

```json
{
  "meta": {
    "case_id": "standard-s001",
    "title": "Cyberpunk City Night — Volumetric Lighting 360°",
    "style": "cyberpunk · sci-fi · hyper-realistic",
    "ar_flag": "--ar 2:1",
    "projection": "equirectangular 360 degree panorama"
  },
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "equirectangular · 完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "8K超高分辨率全景",
    "渲染引擎": "Unreal Engine 5 · Lumen全局光照"
  },
  "相机参数": {
    "焦距": "等效 85mm 全画幅定焦镜头",
    "光圈": "f/1.8 大光圈，夜景虚化",
    "快门": "1/30s 轻微动态模糊",
    "ISO": "ISO 3200 夜景高感",
    "白平衡": "钨丝灯 3200K 偏暖，霓虹冷暖对比"
  },
  "场景构图": {
    "地点": "2089年亚洲风格赛博朋克超级都市，深夜",
    "相机位置": "街道地面中央，十字路口中心点",
    "相机高度": "约1.6米，人视角",
    "视野范围": "水平360度，垂直180度",
    "投影行为": "正确的等距柱状畸变，确保无缝球形拼接",
    "天气状况": "雨后潮湿，地面积水形成完美镜面反射，空气中弥漫轻薄水雾",
    "景深": "中景建筑清晰，远景霓虹灯光有轻微大气散射"
  },
  "视觉元素": {
    "前景": {
      "地面": "潮湿的黑色沥青路面，完美镜面反射霓虹广告和路灯，水坑中倒影细节丰富",
      "物件": "散落的全息投影广告牌碎片、电子垃圾堆、蒸汽排放管道，发出橙色蒸汽",
      "动态": "雨后水面轻微涟漪，全息广告牌图像有轻微扫描线闪烁"
    },
    "中景主体": {
      "建筑群": "360度环绕的高耸摩天大楼，外立面密布霓虹广告牌（日文、中文、英文混合），大量LED屏幕播放广告",
      "交通": "飞行汽车在建筑间穿梭留下光轨，地面有无人驾驶舱车辆通过，磁悬浮轨道横贯中景",
      "人群": "街道两侧有赛博朋克风格行人剪影，穿着发光服饰，部分有机械义体",
      "颜色主调": "品红色 #FF0080 和青色 #00FFFF 的强烈霓虹对比，穿插橙色 #FF6600 钠灯和紫色 #8000FF 激光"
    },
    "背景与天空": {
      "天空半球": "乌云密布的夜空，城市光污染将低云染成橙紫色，偶见闪电",
      "远景建筑": "无数摩天楼轮廓延伸至天际线，顶部红色航空警示灯点缀其间",
      "特效": "容积光（Volumetric Light）从高楼间穿射而下，在水雾中形成丁达尔效应光束"
    },
    "环境氛围": {
      "整体基调": "高科技低生活（High-tech Low-life），压抑又迷幻，充满霓虹灯的超现实感",
      "光影对比": "极强的明暗对比，霓虹光源区域过曝，阴影区域几乎纯黑"
    }
  },
  "渲染风格": {
    "光照": "多源霓虹灯光 + 容积散射光（Volumetric Scattering），无自然光，完全人工照明",
    "调色": "高饱和度霓虹色调，高对比度，阴影深邃，局部色差（Chromatic Aberration）效果",
    "后期效果": "轻微镜头光晕（Lens Flare），雨滴在镜头上的折射效果，大气雾气",
    "质感质量": {
      "精度": "极高精度写实主义，建筑细节、霓虹管道纹理、地面积水反射均需极度真实",
      "拼接": "完美的360度无缝拼接，无接缝断裂，全景过渡自然"
    }
  },
  "AI生成关键词组合": {
    "正向提示词_EN": "equirectangular 360 degree panorama, --ar 2:1, cyberpunk city night, volumetric neon lighting, rain-soaked streets, mirror reflections on wet asphalt, neon signs in Japanese and Chinese, flying cars with light trails, atmospheric fog, Unreal Engine 5 Lumen, ultra-detailed 8K, hyper-realistic, sci-fi megacity, chromatic aberration, lens flare",
    "负面提示词": ["文字叠加", "水印", "边框", "拼接接缝", "白天光照", "自然风景", "过度饱和失真", "插画风格"]
  },
  "约束条件": {
    "必须保留": [
      "equirectangular 360度全景透视",
      "2:1宽高比",
      "雨后地面镜面反射",
      "赛博朋克霓虹配色",
      "容积光效果"
    ],
    "必须避免": [
      "自然光照",
      "非城市场景",
      "卡通或插画风格",
      "拼接断裂",
      "全景接缝"
    ]
  }
}
```

---

## Case S-002 · 瑞士阿尔卑斯山极致自然风光 Epic Swiss Alps

**场景标签 Tags:** `Swiss Alps` `nature` `epic` `mountain` `8K` `golden hour` `snow peak`

**一句话描述:** 瑞士阿尔卑斯山黄金时刻，雪峰、冰川、高山牧场 360° 震撼全景，8K 超高清

**One-liner:** Swiss Alps at golden hour, snow peaks, glaciers, and alpine meadows in stunning 360° panorama, 8K ultra-resolution

### 📋 JSON 提示词

```json
{
  "meta": {
    "case_id": "standard-s002",
    "title": "Epic Swiss Alps — 8K Golden Hour 360° Panorama",
    "style": "photorealistic · nature photography · ultra-detailed",
    "ar_flag": "--ar 2:1",
    "projection": "equirectangular 360 degree panorama"
  },
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "equirectangular · 完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "8K超高分辨率全景（7680×3840像素）",
    "摄影风格": "顶级自然风光摄影，媲美 National Geographic 画质"
  },
  "相机参数": {
    "焦距": "等效 24mm 超广角镜头",
    "光圈": "f/8 大景深，远近均清晰",
    "快门": "1/125s",
    "ISO": "ISO 100 基础感光度，最低噪点",
    "白平衡": "日光 5600K，黄金时刻暖光校正",
    "HDR": "高动态范围合成，保留雪峰高光与草地阴影细节"
  },
  "场景构图": {
    "地点": "瑞士格林德尔瓦尔德（Grindelwald）高山草甸，海拔2000米",
    "相机位置": "高山草甸中央，俯瞰大地",
    "相机高度": "约1.2米，三脚架低位拍摄",
    "视野范围": "水平360度，垂直180度",
    "投影行为": "正确的等距柱状畸变，水平线完整无断裂",
    "天气状况": "晴朗无云，能见度极佳，部分天空有薄卷云",
    "时间": "日落前1小时，黄金时刻（Golden Hour）",
    "景深": "大景深，前景野花至远景雪峰全程清晰"
  },
  "视觉元素": {
    "前景": {
      "植被": "郁郁葱葱的高山草甸，密布金色野花（蒲公英、龙胆）和翠绿牧草，露珠在花瓣上闪烁",
      "细节": "草叶纹理清晰，蜜蜂在花间飞舞，蝴蝶偶尔停驻",
      "地形": "轻微起伏的草地，远处可见传统瑞士木质栅栏"
    },
    "中景主体": {
      "地形特征": "宏伟的阿尔卑斯山谷，翠绿的山坡梯形牧场层层延伸",
      "建筑点缀": "点缀着几座典型的瑞士棕色木屋（Swiss Chalet），烟囱轻烟袅袅",
      "生态": "远处山坡上有一群黑白奶牛悠闲吃草，脖间铜铃隐约可见",
      "冰川": "中景山谷中可见湛蓝色的冰川舌，阳光下熠熠生辉"
    },
    "背景": {
      "山峰": "360度环绕的壮阔雪峰群：正面艾格峰（Eiger 3970m）、僧侣峰（Mönch）、少女峰（Jungfrau 4158m），雪峰在黄金时刻被染成金粉色",
      "天空": "湛蓝的高海拔天空，底层有少量金边卷云，天空渐变从湛蓝到地平线的橙金色",
      "大气": "远山略有淡蓝色大气雾气（Atmospheric Haze），增强空间纵深感"
    },
    "环境氛围": {
      "整体基调": "宏伟、壮阔、纯净、震撼，体现大自然的绝对力量",
      "色彩搭配": "翠绿牧草、金黄野花、蔚蓝天空、纯白雪峰、金色光晕，色彩丰富而和谐"
    }
  },
  "渲染风格": {
    "光照": "黄金时刻低角度斜射暖光，侧向照射使山峰产生强烈立体感，草地呈金色逆光效果",
    "调色": "自然写实，轻度对比度提升，绿色饱和度适当增强，雪峰细节保留完整",
    "大气效果": "远景大气透视，增强空间层次感",
    "质感质量": {
      "精度": "媲美专业摄影师实拍的超高清细节，每一根草叶、每一块岩石纹理均清晰可辨",
      "动态": "草地在微风中轻摇，快门速度足够高冻结动作",
      "拼接": "完美的360度无缝拼接，地平线水平，无畸变断裂"
    }
  },
  "AI生成关键词组合": {
    "正向提示词_EN": "equirectangular 360 degree panorama, --ar 2:1, epic Swiss Alps, Grindelwald, golden hour, Jungfrau snow peak, alpine meadow with wildflowers, Swiss chalet, glacier, hyper-realistic 8K nature photography, National Geographic quality, atmospheric haze, HDR, ultra-detailed, photorealistic",
    "负面提示词": ["水印", "文字", "人物特写", "城市建筑", "拼接接缝", "插画感", "过度HDR色调断裂", "人工痕迹"]
  },
  "约束条件": {
    "必须保留": [
      "equirectangular 360度全景透视",
      "2:1宽高比",
      "瑞士阿尔卑斯雪峰群作为360度背景",
      "黄金时刻光线",
      "高山草甸前景"
    ],
    "必须避免": [
      "任何城市元素",
      "人物特写",
      "虚假感或插画感",
      "拼接断裂或接缝"
    ]
  }
}
```

---

## Case S-003 · 极简禅意室内设计 Minimalist Zen Interior

**场景标签 Tags:** `interior` `minimalist` `zen` `Unreal Engine 5` `architectural visualization` `Japanese` `calm`

**一句话描述:** UE5 渲染的日式禅意极简室内空间，自然光渗透障子纸，360° 沉浸式建筑可视化

**One-liner:** UE5-rendered Japanese Zen minimalist interior, natural light filtering through shoji screens, 360° immersive architectural visualization

### 📋 JSON 提示词

```json
{
  "meta": {
    "case_id": "standard-s003",
    "title": "Minimalist Zen Interior — Unreal Engine 5 360° Render",
    "style": "architectural visualization · minimalist · zen · photorealistic",
    "ar_flag": "--ar 2:1",
    "projection": "equirectangular 360 degree panorama"
  },
  "图像元数据": {
    "类型": "360度等距柱状全景图",
    "投影方式": "equirectangular · 完整球形等距柱状投影",
    "宽高比": "2:1",
    "分辨率": "8K超高分辨率室内渲染全景",
    "渲染引擎": "Unreal Engine 5 · Lumen全局光照 · Nanite超细节网格"
  },
  "相机参数": {
    "焦距": "等效 24mm 超广角镜头（室内全景标准）",
    "光圈": "f/2.8",
    "快门": "1/60s",
    "ISO": "ISO 400",
    "白平衡": "自然日光 5500K，室内木质温暖补偿"
  },
  "场景构图": {
    "地点": "日式极简禅意冥想室，现代日本私人住宅内",
    "相机位置": "房间正中央地板，坐禅视角",
    "相机高度": "约0.5米，席地而坐的视角",
    "视野范围": "水平360度，垂直180度（包含天花板和地板全景）",
    "投影行为": "正确的等距柱状畸变，室内透视正确，无桶形畸变",
    "天气状况": "晴天，柔和的漫射自然光通过障子纸过滤",
    "时间": "午后，自然光最柔和的时段"
  },
  "视觉元素": {
    "天花板": {
      "材质": "原木色桧木（Hinoki Cypress）横梁结构裸露，表面纹理细腻",
      "照明": "隐藏式LED槽灯提供极为均匀的漫射环境光，无明显光源"
    },
    "墙壁": {
      "障子门": "360度四面均有传统日式障子纸推拉门（Shoji Screen），半透明和纸过滤窗外阳光，形成柔和光斑",
      "质感": "部分墙面为原始混凝土（Wabi-Sabi 美学），部分为抹灰白墙，质感粗糙而精致"
    },
    "地面": {
      "材质": "传统榻榻米（Tatami）地板，草编纹理极度清晰，散发淡淡绿色光泽",
      "陈设": "房间中央一个圆形低矮茶几（黑色漆器），茶几上摆放一套简洁的日式茶具",
      "装饰": "角落一个简单的竹制插花（一枝白玫瑰，一枝绿竹），旁边有一方小砂石禅园（Zen Garden）"
    },
    "窗外景观": {
      "室外": "障子纸背后可隐约看到传统日式枯山水庭院的轮廓，石灯笼剪影，苔藓石板",
      "植物": "室内角落有一盆大型橡皮树，自然简洁"
    },
    "光线特效": {
      "光束": "午后斜射阳光穿透障子纸，在房间内形成柔和的矩形光斑，边缘渐变",
      "尘埃": "阳光中可见轻微飘浮的尘埃粒子（Dust Particles），增强空间真实感",
      "影子": "障子格栅在地面和墙上投下精确的网格状阴影，随时间缓慢移动"
    }
  },
  "环境氛围": {
    "整体基调": "极简、宁静、禅意、空灵，时间仿佛静止，令人心静",
    "色彩搭配": "原木米色 #D4A96A、榻榻米草绿 #8FA86B、混凝土灰 #9B9B8A、纯白障子 #F5F5F0，极低饱和度，高雅克制",
    "噪音元素": "零杂乱，每件物品均有其意义，留白是设计的核心"
  },
  "渲染风格": {
    "光照": "Unreal Engine 5 Lumen实时全局光照，完全基于物理的（PBR）光线追踪渲染，无任何人工补光痕迹",
    "材质": "每种材质均需次表面散射（SSS）处理：障子纸半透明散射、榻榻米草编纤维质感、原木微观纹理",
    "调色": "低饱和度、高质感，轻微暖色调，避免任何鲜艳颜色，保持禅意克制",
    "质感质量": {
      "精度": "Nanite超高精度网格，每一根草席纤维、每一处木纹均清晰可辨",
      "光照准确性": "物理准确的室内全局光照，无任何 artifacts 或漏光",
      "拼接": "完美的360度无缝室内全景，地面到天花板的垂直180度均正确渲染"
    }
  },
  "AI生成关键词组合": {
    "正向提示词_EN": "equirectangular 360 degree panorama, --ar 2:1, minimalist Zen interior design, Japanese Wabi-Sabi aesthetic, tatami floor, shoji screen with diffused natural light, hinoki cypress ceiling beams, tea ceremony setup, dust particles in light, Unreal Engine 5 Lumen photorealistic render, 8K architectural visualization, ultra-detailed materials, PBR rendering, serene tranquil atmosphere",
    "负面提示词": ["现代西式家具", "强烈色彩", "杂乱陈设", "人物", "科技产品", "荧光灯", "拼接接缝", "渲染瑕疵", "过曝", "人工感光照"]
  },
  "约束条件": {
    "必须保留": [
      "equirectangular 360度全景透视（含天花板和地板）",
      "2:1宽高比",
      "障子纸漫射自然光为主光源",
      "榻榻米地面",
      "极简禅意氛围",
      "UE5级别渲染质量"
    ],
    "必须避免": [
      "西式家具",
      "强烈颜色",
      "渲染瑕疵",
      "拼接断裂",
      "任何文字或标志"
    ]
  }
}
```

---

## 📌 使用说明 · Usage Notes

### 必须包含的核心参数 · Mandatory Core Parameters

所有 360° 全景提示词必须包含以下两个关键参数，缺一不可：

```
--ar 2:1                              (宽高比 2:1，等距柱状投影标准)
equirectangular 360 degree panorama   (投影方式声明，告知 AI 生成全景)
```

### 推荐工具 · Recommended AI Tools

| 工具 Tool | 全景质量 Quality | 格式支持 | 备注 |
|:---|:---:|:---:|:---|
| GPT Image (gpt-image-1) | ⭐⭐⭐⭐⭐ | 2:1 natively | 最佳全景效果 |
| DALL·E 3 | ⭐⭐⭐⭐ | 需指定 2:1 | 稳定可靠 |
| Midjourney v6 | ⭐⭐⭐⭐ | `--ar 2:1` | 艺术感强 |
| Stable Diffusion | ⭐⭐⭐ | 需插件 | 可控性最高 |

### 进阶提升 · Advanced Upscaling

生成基础图后，参考仓库主页 README 中的 **全景分辨率突破方案** 进行：
1. ControlNet Tile 切片重绘（×4 超分）
2. PTGui Pro 无缝拼接
3. 最终输出 16K~32K 超高清 VR 全景

---

*更多提示词案例请访问 [绘梦拾光 (diysq.com)](https://www.diysq.com)*
