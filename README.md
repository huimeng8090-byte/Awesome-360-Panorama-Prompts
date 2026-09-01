# 🌍 Awesome 360° Panorama Prompts

> 最大的开源 360° 全景图提示词库 · 从 [DIYSQ.com](https://www.diysq.com) 自动同步

[![在线预览](https://img.shields.io/badge/🌐_在线预览-点击交互浏览-2ea44f?style=for-the-badge)](https://huimeng8090-byte.github.io/Awesome-360-Panorama-Prompts/)

本仓库收录 **445** 条 360° 全景图提示词，每条包含完整的结构化 JSON，可直接用于 GPT Image 等模型生成无缝拼接的等距柱状投影（Equirectangular）全景图。

## ✨ 特性

- 🤖 **GPT Image 兼容** — 结构化 JSON 格式，直接粘贴即可生成
- 🥽 **VR Ready** — 标准 2:1 等距柱状投影，支持 Pannellum / Krpano
- 📄 **JSON Format** — 全景规范、场景描述、光影氛围、材质细节、负面约束
- 🔄 **自动同步** — GitHub Actions 每天自动从 diysq.com 拉取最新内容
- 🖼️ **预览图** — 每条提示词附带生成效果预览

## 📂 目录结构

```
├── prompts/          # 提示词 JSON 文件
├── images/           # 预览图
├── scripts/sync.py   # 同步脚本
├── .github/workflows # 自动同步工作流
└── index.html        # 在线演示页
```

## 🖼️ 全部提示词

**分类导航：** [360全景视觉 (159)](#360全景视觉) · [GPT Image 2.0 (87)](#gpt-image-2.0) · [景区 (75)](#景区) · [街头 (25)](#街头) · [客厅 (23)](#客厅) · [人物 (15)](#人物) · [插画 (14)](#插画) · [花 (10)](#花) · [游戏场景 (7)](#游戏场景) · [科幻场景 (7)](#科幻场景) · [古建筑 (6)](#古建筑) · [动物 (4)](#动物) · [建筑 (4)](#建筑) · [瀑布 (4)](#瀑布) · [酒店 (3)](#酒店) · [海底世界 (2)](#海底世界)

### 360全景视觉 (159 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case033](images/case033/output.jpg) | 北境苔原上的驯鹿守望｜亚极地高山丘陵360沉浸式全景 | GPT Image | 2026-08-24 | [JSON](prompts/case033.json) |
| ![case299](images/case299/output.jpg) | 春日梯田大地颂歌·360全景提示词 | GPT Image | 2026-04-17 | [JSON](prompts/case299.json) |
| ![case300](images/case300/output.jpg) | 万物复苏云巅梯田春色沉浸式空间全景提示词 | GPT Image | 2026-04-17 | [JSON](prompts/case300.json) |
| ![case301](images/case301/output.jpg) | 金色黄昏下的蒲公英花田360全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case301.json) |
| ![case302](images/case302/output.jpg) | 冰岛春日花海瀑布全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case302.json) |
| ![case303](images/case303/output.jpg) | 梦幻春日大地：繁花梯田与孤傲樱树 360 全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case303.json) |
| ![case304](images/case304/output.jpg) | 金山玉幕·360度春天雪山日落梯田奇观全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case304.json) |
| ![case305](images/case305/output.jpg) | 春日雏菊花海超低机位沉浸全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case305.json) |
| ![case306](images/case306/output.jpg) | 湖畔漫步：16米人眼高度360度沉浸全景提示词 | GPT Image | 2026-04-16 | [JSON](prompts/case306.json) |
| ![case307](images/case307/output.jpg) | 幻境之巅：银河拱门下的云端天梯360全景提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case307.json) |
| ![case308](images/case308/output.jpg) | 星轨云海下的山巅灯火 360全景提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case308.json) |
| ![case309](images/case309/output.jpg) | 暮色苍穹：雪国极巅的360度全景颂歌提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case309.json) |
| ![case310](images/case310/output.jpg) | 春日林地全景，花海与晨光的洗礼提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case310.json) |
| ![case311](images/case311/output.jpg) | 欧式庄园春日郁金香360全景提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case311.json) |
| ![case312](images/case312/output.jpg) | 春意盎然：微距视界下的360全景宇宙提示词 | GPT Image | 2026-04-14 | [JSON](prompts/case312.json) |
| ![case313](images/case313/output.jpg) | 莫斯科：新圣女修道院之夜 | GPT Image | 2026-04-11 | [JSON](prompts/case313.json) |
| ![case314](images/case314/output.jpg) | 高原俯视：红土地质的宏大指纹 | GPT Image | 2026-04-11 | [JSON](prompts/case314.json) |
| ![case315](images/case315/output.jpg) | 纪念碑谷：图腾柱的时间之塔 | GPT Image | 2026-04-11 | [JSON](prompts/case315.json) |
| ![case316](images/case316/output.jpg) | 死亡谷：红沙丘与千年枯木 | GPT Image | 2026-04-11 | [JSON](prompts/case316.json) |
| ![case317](images/case317/output.jpg) | 死谷恶水盆地：盐碱之花的几何 | GPT Image | 2026-04-11 | [JSON](prompts/case317.json) |
| ![case318](images/case318/output.jpg) | 伊瓜苏：雨林之巅的圣水 | GPT Image | 2026-04-11 | [JSON](prompts/case318.json) |
| ![case319](images/case319/output.jpg) | 纳瓦霍高原：光影雕琢的迷宫 | GPT Image | 2026-04-11 | [JSON](prompts/case319.json) |
| ![case320](images/case320/output.jpg) | 纪念碑谷：史诗般的晚霞孤峰 | GPT Image | 2026-04-11 | [JSON](prompts/case320.json) |
| ![case321](images/case321/output.jpg) | 悉尼港：世界级都市海港全景 | GPT Image | 2026-04-11 | [JSON](prompts/case321.json) |
| ![case322](images/case322/output.jpg) | 亚利桑那州：马蹄湾翡翠之环 | GPT Image | 2026-04-11 | [JSON](prompts/case322.json) |
| ![case323](images/case323/output.jpg) | 60度绝美海岛全景图：碧海、金沙与绿岛 | GPT Image | 2026-04-05 | [JSON](prompts/case323.json) |
| ![case324](images/case324/output.jpg) | 拉贾安帕特：360度热带群岛航拍全景 | GPT Image | 2026-04-05 | [JSON](prompts/case324.json) |
| ![case325](images/case325/output.jpg) | 拉贾安帕特喀斯特群岛高空全景 | GPT Image | 2026-04-05 | [JSON](prompts/case325.json) |
| ![case326](images/case326/output.jpg) | 航拍拉贾安帕特群岛：黎明时分梦幻般的喀斯特海景 | GPT Image | 2026-04-05 | [JSON](prompts/case326.json) |
| ![case327](images/case327/output.jpg) | 四王群岛，360度空中全景：遗失的蓝色天堂 | GPT Image | 2026-04-05 | [JSON](prompts/case327.json) |
| ![case328](images/case328/output.jpg) | 龙目岛吉利群岛的高空无缝360全景 | GPT Image | 2026-04-05 | [JSON](prompts/case328.json) |
| ![case329](images/case329/output.jpg) | 光影赞歌：塞洛姆主峰的日照金山360度落日全景 | GPT Image | 2026-04-05 | [JSON](prompts/case329.json) |
| ![case330](images/case330/output.jpg) | 山河咏叹：塔吉姆峡谷与阿萨河的360度田园诗画 | GPT Image | 2026-04-05 | [JSON](prompts/case330.json) |
| ![case331](images/case331/output.jpg) | 暮色金顶：塞洛姆山脊的360度黄昏全景史诗 | GPT Image | 2026-04-05 | [JSON](prompts/case331.json) |
| ![case332](images/case332/output.jpg) | 云端救赎：里约基督像与日照金山全景提示词 | GPT Image | 2026-04-05 | [JSON](prompts/case332.json) |
| ![case333](images/case333/output.jpg) | 极地冰雪日落，360度航拍全景提示词 | GPT Image | 2026-04-05 | [JSON](prompts/case333.json) |
| ![case334](images/case334/output.jpg) | 阿尔及利亚塔西里·纳杰尔（Tassili n8217Ajjer）沙漠与石林 360 全景：壮阔的自然... | GPT Image | 2026-04-05 | [JSON](prompts/case334.json) |
| ![case335](images/case335/output.jpg) | 堪察加火山湖与云海全景：自然的极致壮丽 | GPT Image | 2026-04-05 | [JSON](prompts/case335.json) |
| ![case336](images/case336/output.jpg) | 梦幻云海：黄山奇峰360度航拍全景提示词 | GPT Image | 2026-04-05 | [JSON](prompts/case336.json) |
| ![case337](images/case337/output.jpg) | 360度高空无人机视角下雄伟的梯田群山 | GPT Image | 2026-04-05 | [JSON](prompts/case337.json) |
| ![case338](images/case338/output.jpg) | 云巅之上的自然史诗：哈尼梯田日出全景提示词 | GPT Image | 2026-03-27 | [JSON](prompts/case338.json) |
| ![case339](images/case339/output.jpg) | 阿尔及利亚撒哈拉沙漠峡谷地貌正午 360 全景航拍 | GPT Image | 2026-03-22 | [JSON](prompts/case339.json) |
| ![case340](images/case340/output.jpg) | 西伯利亚苔原湿地曲流河 360 全景航拍 | GPT Image | 2026-03-22 | [JSON](prompts/case340.json) |
| ![case341](images/case341/output.jpg) | 上海陆家嘴黄浦江日出 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case341.json) |
| ![case342](images/case342/output.jpg) | 约旦瓦迪拉姆沙漠峡谷地貌正午 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case342.json) |
| ![case343](images/case343/output.jpg) | 黄山花岗岩峰林云海 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case343.json) |
| ![case344](images/case344/output.jpg) | 堪察加半岛火山与火山湖 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case344.json) |
| ![case345](images/case345/output.jpg) | 南极半岛冰雪海湾日出 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case345.json) |
| ![case346](images/case346/output.jpg) | 约旦瓦迪拉姆沙漠峡谷地貌正午 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case346.json) |
| ![case347](images/case347/output.jpg) | 里约热内卢基督像云海日出 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case347.json) |
| ![case348](images/case348/output.jpg) | 云南元阳梯田日出 360 全景航拍 | GPT Image | 2026-03-21 | [JSON](prompts/case348.json) |
| ![case349](images/case349/output.jpg) | 撒哈拉沙漠沙丘戈壁地貌 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case349.json) |
| ![case350](images/case350/output.jpg) | 伊瓜苏大瀑布群彩虹奇观 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case350.json) |
| ![case351](images/case351/output.jpg) | 安第斯高原地热池与湖泊 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case351.json) |
| ![case352](images/case352/output.jpg) | 纳米布沙漠峡谷地貌日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case352.json) |
| ![case353](images/case353/output.jpg) | 天山山脉戈壁雪原日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case353.json) |
| ![case354](images/case354/output.jpg) | 张掖七彩丹霞彩色丘陵正午 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case354.json) |
| ![case355](images/case355/output.jpg) | 约旦瓦迪拉姆沙漠峡谷地貌 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case355.json) |
| ![case356](images/case356/output.jpg) | 阿尔泰山区蛇形曲流河峡谷 360 全景航拍》 | GPT Image | 2026-03-20 | [JSON](prompts/case356.json) |
| ![case357](images/case357/output.jpg) | 冰岛高地苔原秋季彩林与湖泊 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case357.json) |
| ![case358](images/case358/output.jpg) | 黄山花岗岩峰林日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case358.json) |
| ![case359](images/case359/output.jpg) | 加勒比海群岛珊瑚礁海域 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case359.json) |
| ![case360](images/case360/output.jpg) | 阿尔泰山区曲流河与雪山日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case360.json) |
| ![case361](images/case361/output.jpg) | 堪察加荒野溪流棕熊栖息地 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case361.json) |
| ![case362](images/case362/output.jpg) | 黄山花岗岩峰林晨雾 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case362.json) |
| ![case363](images/case363/output.jpg) | 莫斯科克里姆林宫教堂群日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case363.json) |
| ![case364](images/case364/output.jpg) | 芝加哥城市天际线日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case364.json) |
| ![case365](images/case365/output.jpg) | 加勒比海热带珊瑚礁群岛 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case365.json) |
| ![case366](images/case366/output.jpg) | 张掖七彩丹霞彩色丘陵日出 360 全景航拍 | GPT Image | 2026-03-20 | [JSON](prompts/case366.json) |
| ![case367](images/case367/output.jpg) | 印尼四王岛热带群岛珊瑚礁海域 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case367.json) |
| ![case368](images/case368/output.jpg) | 南极极地雪原冰湖荒原 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case368.json) |
| ![case369](images/case369/output.jpg) | 北海道秋季火山湖群 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case369.json) |
| ![case370](images/case370/output.jpg) | 张掖七彩丹霞彩色丘陵侧光 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case370.json) |
| ![case371](images/case371/output.jpg) | 堪察加锥形火山云海日出 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case371.json) |
| ![case372](images/case372/output.jpg) | 亚马逊热带雨林流域原生地貌 360 全景航拍 | GPT Image | 2026-03-19 | [JSON](prompts/case372.json) |
| ![case373](images/case373/output.jpg) | 雪林秘境：芬兰拉普兰雪林的日出盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case373.json) |
| ![case374](images/case374/output.jpg) | 冰镜岩岛：贝加尔湖冰裂镜面的日落盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case374.json) |
| ![case375](images/case375/output.jpg) | 蓝湖秋境：堪察加地热蓝湖的秋日盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case375.json) |
| ![case376](images/case376/output.jpg) | 黄山奇境：黄山花岗岩峰林的日出丁达尔盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case376.json) |
| ![case377](images/case377/output.jpg) | 绿野九曲：堪察加原始湿地的河曲湖境盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case377.json) |
| ![case378](images/case378/output.jpg) | 彩谷秘境：阿尔泰五彩河谷的丹霞峡谷盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case378.json) |
| ![case379](images/case379/output.jpg) | 彩丘神迹：张掖丹霞地貌的红层丘陵盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case379.json) |
| ![case380](images/case380/output.jpg) | 梯田天境：元阳哈尼梯田的日出云海盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case380.json) |
| ![case381](images/case381/output.jpg) | 金沙瀚海：撒哈拉沙漠新月沙丘的正午盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case381.json) |
| ![case382](images/case382/output.jpg) | 冰裂岩岛：贝加尔湖碎冰蓝冰的凛冬奇景 | GPT Image | 2026-03-10 | [JSON](prompts/case382.json) |
| ![case383](images/case383/output.jpg) | 火山湖境：堪察加火山群的冰斗湖日出盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case383.json) |
| ![case384](images/case384/output.jpg) | 雪原冰脉：极北冬日冰封雪原的正午盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case384.json) |
| ![case385](images/case385/output.jpg) | 彩谷烟岚：地热峡谷的多彩喷烟奇景 | GPT Image | 2026-03-10 | [JSON](prompts/case385.json) |
| ![case386](images/case386/output.jpg) | 火山圣境：印尼布罗莫火山的日出奇景 | GPT Image | 2026-03-10 | [JSON](prompts/case386.json) |
| ![case387](images/case387/output.jpg) | 蒸汽秘境：地热火山带的翻涌云海奇景 | GPT Image | 2026-03-10 | [JSON](prompts/case387.json) |
| ![case388](images/case388/output.jpg) | 瀚海戈壁：撒哈拉沙漠的风蚀岩漠日落盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case388.json) |
| ![case389](images/case389/output.jpg) | 极地冰境：南极半岛的冰雪海湾日落盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case389.json) |
| ![case390](images/case390/output.jpg) | 巴西伦索伊斯马拉赫塞斯的沙漠奇景 | GPT Image | 2026-03-10 | [JSON](prompts/case390.json) |
| ![case391](images/case391/output.jpg) | 云巅之上：北美雪山云海的日出盛景 | GPT Image | 2026-03-10 | [JSON](prompts/case391.json) |
| ![case392](images/case392/output.jpg) | 蓝海秘境：加勒比热带海岛的日落金辉 | GPT Image | 2026-03-10 | [JSON](prompts/case392.json) |
| ![case393](images/case393/output.jpg) | 古城回响：马丘比丘云端之城的全景秘境 | GPT Image | 2026-03-05 | [JSON](prompts/case393.json) |
| ![case394](images/case394/output.jpg) | 沙漠未来：迪拜棕榈岛的人造奇迹航拍 | GPT Image | 2026-03-05 | [JSON](prompts/case394.json) |
| ![case395](images/case395/output.jpg) | 爱琴海之吻：圣托里尼的蓝白浪漫全景 | GPT Image | 2026-03-05 | [JSON](prompts/case395.json) |
| ![case396](images/case396/output.jpg) | 冰与火之歌：瓦特纳冰川的幽蓝深处 | GPT Image | 2026-03-05 | [JSON](prompts/case396.json) |
| ![case397](images/case397/output.jpg) | 雷鸣之烟：维多利亚大瀑布的垂直震撼 | GPT Image | 2026-03-05 | [JSON](prompts/case397.json) |
| ![case398](images/case398/output.jpg) | 大地调色盘：张掖丹霞的斑斓地质史诗 | GPT Image | 2026-03-05 | [JSON](prompts/case398.json) |
| ![case399](images/case399/output.jpg) | 云海松风：黄山奇峰的仙境全景 | GPT Image | 2026-03-05 | [JSON](prompts/case399.json) |
| ![case400](images/case400/output.jpg) | 金色脊线：撒哈拉沙漠的极简光影史诗 | GPT Image | 2026-03-05 | [JSON](prompts/case400.json) |
| ![case401](images/case401/output.jpg) | 水墨浮城：威尼斯水网的沉浸式历史画卷 | GPT Image | 2026-03-05 | [JSON](prompts/case401.json) |
| ![case402](images/case402/output.jpg) | 世界之巅：喜马拉雅珠穆朗玛峰的宏伟群峰 | GPT Image | 2026-03-03 | [JSON](prompts/case402.json) |
| ![case403](images/case403/output.jpg) | 永恒对称：印度泰姬陵与亚穆纳河的圣洁清晨 | GPT Image | 2026-03-03 | [JSON](prompts/case403.json) |
| ![case404](images/case404/output.jpg) | 沙海幻境：纳米布沙漠红色沙丘与罕见平流云海 | GPT Image | 2026-03-03 | [JSON](prompts/case404.json) |
| ![case405](images/case405/output.jpg) | 千岛迷宫：拉贾安帕特群岛的翡翠珍珠与清澈海域 | GPT Image | 2026-03-03 | [JSON](prompts/case405.json) |
| ![case406](images/case406/output.jpg) | 永恒丰碑：吉萨大金字塔群与撒哈拉沙漠的落日余晖 | GPT Image | 2026-03-03 | [JSON](prompts/case406.json) |
| ![case407](images/case407/output.jpg) | 地球脉动：堪察加半岛深秋火山与色彩斑斓的苔原 | GPT Image | 2026-03-03 | [JSON](prompts/case407.json) |
| ![case408](images/case408/output.jpg) | 地狱之喉：汹涌磅礴的伊瓜苏马蹄形大瀑布 | GPT Image | 2026-03-03 | [JSON](prompts/case408.json) |
| ![case409](images/case409/output.jpg) | 极寒巅峰：瑞士阿尔卑斯山脉的银色冰雪荒原 | GPT Image | 2026-03-03 | [JSON](prompts/case409.json) |
| ![case410](images/case410/output.jpg) | 加勒比之光：清澈如镜的青绿色离岛与珊瑚礁 | GPT Image | 2026-03-03 | [JSON](prompts/case410.json) |
| ![case411](images/case411/output.jpg) | 云巔神迹：巴西里约救世基督像与壮丽云海 | GPT Image | 2026-03-03 | [JSON](prompts/case411.json) |
| ![case412](images/case412/output.jpg) | 生命律动：蒙古大草原上的普氏野马群自由奔袭 | GPT Image | 2026-03-03 | [JSON](prompts/case412.json) |
| ![case413](images/case413/output.jpg) | 张掖七彩丹霞地貌360度航拍全景 | GPT Image | 2026-03-02 | [JSON](prompts/case413.json) |
| ![case414](images/case414/output.jpg) | 阿杰尔高原岩林与沙丘360度全景 | GPT Image | 2026-03-02 | [JSON](prompts/case414.json) |
| ![case415](images/case415/output.jpg) | 撒哈拉线性沙丘日落360度航拍全景 | GPT Image | 2026-03-02 | [JSON](prompts/case415.json) |
| ![case416](images/case416/output.jpg) | 南极洲冰山与极地海域360度航拍全景 | GPT Image | 2026-03-02 | [JSON](prompts/case416.json) |
| ![case417](images/case417/output.jpg) | 迪拜哈利法塔夜景360度航拍全景 | GPT Image | 2026-03-02 | [JSON](prompts/case417.json) |
| ![case418](images/case418/output.jpg) | 上海陆家嘴摩天大楼夜景360度全景 | GPT Image | 2026-03-02 | [JSON](prompts/case418.json) |
| ![case419](images/case419/output.jpg) | 普托拉纳平原玄武岩峡谷秋色全景 | GPT Image | 2026-03-02 | [JSON](prompts/case419.json) |
| ![case420](images/case420/output.jpg) | 拉普兰极地雪树森林日落360度全景 | GPT Image | 2026-03-02 | [JSON](prompts/case420.json) |
| ![case421](images/case421/output.jpg) | 撒哈拉U型沙丘盆地360度航拍全景 | GPT Image | 2026-03-02 | [JSON](prompts/case421.json) |
| ![case422](images/case422/output.jpg) | 堪察加火山喷发雪景 | GPT Image | 2026-03-01 | [JSON](prompts/case422.json) |
| ![case423](images/case423/output.jpg) | 高原镜面湖泊与山脉 | GPT Image | 2026-03-01 | [JSON](prompts/case423.json) |
| ![case424](images/case424/output.jpg) | 埃及吉萨金字塔群沙漠航拍 | GPT Image | 2026-03-01 | [JSON](prompts/case424.json) |
| ![case425](images/case425/output.jpg) | 张掖七彩丹霞360日出全景 | GPT Image | 2026-03-01 | [JSON](prompts/case425.json) |
| ![case426](images/case426/output.jpg) | 格陵兰迪斯科湾巨型冰山360全景 | GPT Image | 2026-03-01 | [JSON](prompts/case426.json) |
| ![case427](images/case427/output.jpg) | 波罗的海狭长海岸森林360航拍全景 | GPT Image | 2026-03-01 | [JSON](prompts/case427.json) |
| ![case428](images/case428/output.jpg) | 北极冰封海面日出360全景 | GPT Image | 2026-03-01 | [JSON](prompts/case428.json) |
| ![case429](images/case429/output.jpg) | 拉普兰雾凇雪林日出360全景 | GPT Image | 2026-03-01 | [JSON](prompts/case429.json) |
| ![case430](images/case430/output.jpg) | 泰姬陵360航拍全景 | GPT Image | 2026-03-01 | [JSON](prompts/case430.json) |
| ![case431](images/case431/output.jpg) | 自然风景户外山林草地商业照片 | GPT Image | 2026-03-01 | [JSON](prompts/case431.json) |
| ![case432](images/case432/output.jpg) | 自然风景户外山林草地商业照片 | GPT Image | 2026-03-01 | [JSON](prompts/case432.json) |
| ![case433](images/case433/output.jpg) | 自然风光雪山森林湖泊倒影商业照片 | GPT Image | 2026-03-01 | [JSON](prompts/case433.json) |
| ![case434](images/case434/output.jpg) | 秋季富士山湖泊森林风景商业照片 | GPT Image | 2026-03-01 | [JSON](prompts/case434.json) |
| ![case435](images/case435/output.jpg) | 秋季山林湖泊自然风光照片 | GPT Image | 2026-03-01 | [JSON](prompts/case435.json) |
| ![case436](images/case436/output.jpg) | 自然风光雪山湖泊秋色照片 | GPT Image | 2026-03-01 | [JSON](prompts/case436.json) |
| ![case437](images/case437/output.jpg) | 自然风光山水森林湖泊倒影照片 | GPT Image | 2026-03-01 | [JSON](prompts/case437.json) |
| ![case438](images/case438/output.jpg) | 自然风景山脉森林湖泊倒影商业照片 | GPT Image | 2026-03-01 | [JSON](prompts/case438.json) |
| ![case439](images/case439/output.jpg) | 约书亚树国家公园的日落盛景 | GPT Image | 2026-03-01 | [JSON](prompts/case439.json) |
| ![case440](images/case440/output.jpg) | 青碧河流环绕的山间小镇 | GPT Image | 2026-03-01 | [JSON](prompts/case440.json) |
| ![case441](images/case441/output.jpg) | 高山草甸上的彩虹与繁花邂逅 | GPT Image | 2026-03-01 | [JSON](prompts/case441.json) |
| ![case442](images/case442/output.jpg) | 日落时的沙漠全景 | GPT Image | 2026-03-01 | [JSON](prompts/case442.json) |
| ![case443](images/case443/output.jpg) | 宁静湖泊全景，倒映着雪山与多云蓝天 | GPT Image | 2026-03-01 | [JSON](prompts/case443.json) |
| ![case444](images/case444/output.jpg) | 高山场景全景，彩虹横跨 | GPT Image | 2026-03-01 | [JSON](prompts/case444.json) |
| ![case445](images/case445/output.jpg) | 日落全景，温暖的金紫色天空 | GPT Image | 2026-03-01 | [JSON](prompts/case445.json) |
| ![case446](images/case446/output.jpg) | 秋季山谷湖泊全景 | GPT Image | 2026-03-01 | [JSON](prompts/case446.json) |
| ![case447](images/case447/output.jpg) | 青绿色河流分隔的如画小镇航拍全景 | GPT Image | 2026-03-01 | [JSON](prompts/case447.json) |
| ![case448](images/case448/output.jpg) | 约书亚树沙漠的日落颂歌 | GPT Image | 2026-03-01 | [JSON](prompts/case448.json) |
| ![case449](images/case449/output.jpg) | 雪山湖泊的镜像之美 | GPT Image | 2026-03-01 | [JSON](prompts/case449.json) |
| ![case450](images/case450/output.jpg) | 高山草甸的野花与虹光 | GPT Image | 2026-03-01 | [JSON](prompts/case450.json) |
| ![case451](images/case451/output.jpg) | 日出时分的约书亚树沙漠 | GPT Image | 2026-03-01 | [JSON](prompts/case451.json) |
| ![case452](images/case452/output.jpg) | 秋日山谷的彩林与蓝湖 | GPT Image | 2026-03-01 | [JSON](prompts/case452.json) |
| ![case453](images/case453/output.jpg) | 青川环绕的山间小镇 | GPT Image | 2026-03-01 | [JSON](prompts/case453.json) |
| ![case454](images/case454/output.jpg) | 高山草甸的野花与虹光 | GPT Image | 2026-03-01 | [JSON](prompts/case454.json) |
| ![case455](images/case455/output.jpg) | 河畔的多彩小镇 | GPT Image | 2026-03-01 | [JSON](prompts/case455.json) |
| ![case456](images/case456/output.jpg) | 平静湖泊全景，倒映着雪山与多云天空 | GPT Image | 2026-03-01 | [JSON](prompts/case456.json) |

### GPT Image 2.0 (87 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case212](images/case212/output.jpg) | GPT Image 20提示词｜海岸暮光客厅 | GPT Image | 2026-06-19 | [JSON](prompts/case212.json) |
| ![case213](images/case213/output.jpg) | GPT Image 20全景提示词 复古工业浴境 | GPT Image | 2026-06-19 | [JSON](prompts/case213.json) |
| ![case214](images/case214/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-19 | [JSON](prompts/case214.json) |
| ![case215](images/case215/output.jpg) | GPT Image 20提示词｜复古乡村卧室360全景写实摄影 | GPT Image | 2026-06-19 | [JSON](prompts/case215.json) |
| ![case216](images/case216/output.jpg) | GPT Image 20提示词：360火山黑沙滩史诗级日落全景 | GPT Image | 2026-06-18 | [JSON](prompts/case216.json) |
| ![case217](images/case217/output.jpg) | GPT Image 20提示词：魔幻时刻360巴塔哥尼亚高山湖全景 | GPT Image | 2026-06-18 | [JSON](prompts/case217.json) |
| ![case218](images/case218/output.jpg) | 晨曦孤峰秘境｜GPT Image 20提示词全景写实巨制 | GPT Image | 2026-06-18 | [JSON](prompts/case218.json) |
| ![case219](images/case219/output.jpg) | GPT Image 20提示词｜冰岛蝙蝠山360雪境穹顶全景 | GPT Image | 2026-06-18 | [JSON](prompts/case219.json) |
| ![case220](images/case220/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-17 | [JSON](prompts/case220.json) |
| ![case221](images/case221/output.jpg) | GPT Image 20提示词｜中世纪古镇360全景写实街景 | GPT Image | 2026-06-17 | [JSON](prompts/case221.json) |
| ![case222](images/case222/output.jpg) | GPT Image 20提示词：锈蚀老车环绕式全景街景 | GPT Image | 2026-06-17 | [JSON](prompts/case222.json) |
| ![case223](images/case223/output.jpg) | GPT Image 20提示词｜英伦红色电话亭海湾360超写实全景 | GPT Image | 2026-06-17 | [JSON](prompts/case223.json) |
| ![case224](images/case224/output.jpg) | GPT Image 20提示词全景航拍 | GPT Image | 2026-06-17 | [JSON](prompts/case224.json) |
| ![case225](images/case225/output.jpg) | 极简混凝土纪念装置GPT Image 20提示词 | GPT Image | 2026-06-16 | [JSON](prompts/case225.json) |
| ![case226](images/case226/output.jpg) | 墙面光影裂隙GPT Image 20提示词 | GPT Image | 2026-06-16 | [JSON](prompts/case226.json) |
| ![case227](images/case227/output.jpg) | GPT Image 20提示词极简监控空间 | GPT Image | 2026-06-16 | [JSON](prompts/case227.json) |
| ![case228](images/case228/output.jpg) | GPT Image 20提示词：360黄花菜花海全景写实摄影 | GPT Image | 2026-06-15 | [JSON](prompts/case228.json) |
| ![case229](images/case229/output.jpg) | GPT Image 20提示词：湖畔码头皮划艇360全景写实风光 | GPT Image | 2026-06-15 | [JSON](prompts/case229.json) |
| ![case230](images/case230/output.jpg) | GPT Image 20提示词：地中海松林露天餐厅360全景写实摄影 | GPT Image | 2026-06-15 | [JSON](prompts/case230.json) |
| ![case231](images/case231/output.jpg) | GPT Image 20提示词：360全景荷兰风车草甸超写实摄影 | GPT Image | 2026-06-15 | [JSON](prompts/case231.json) |
| ![case232](images/case232/output.jpg) | GPT Image 20提示词：金色时刻野生海岸花海360全景秘境 | GPT Image | 2026-06-12 | [JSON](prompts/case232.json) |
| ![case233](images/case233/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-12 | [JSON](prompts/case233.json) |
| ![case234](images/case234/output.jpg) | GPT Image 20提示词：昆虫视角草甸日落360全景秘境 | GPT Image | 2026-06-12 | [JSON](prompts/case234.json) |
| ![case235](images/case235/output.jpg) | 冬境芦苇穹顶｜GPT Image 20全景湿地提示词 | GPT Image | 2026-06-12 | [JSON](prompts/case235.json) |
| ![case236](images/case236/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-11 | [JSON](prompts/case236.json) |
| ![case237](images/case237/output.jpg) | GPT Image 20提示词：多洛米蒂布莱耶斯湖360黎明全景 | GPT Image | 2026-06-11 | [JSON](prompts/case237.json) |
| ![case238](images/case238/output.jpg) | 穿越砂岩之门：GPT Image 20提示词打造360史诗级全景奇观 | GPT Image | 2026-06-11 | [JSON](prompts/case238.json) |
| ![case239](images/case239/output.jpg) | GPT Image 20提示词：史诗级罗弗敦群岛360风暴日落全景 | GPT Image | 2026-06-11 | [JSON](prompts/case239.json) |
| ![case240](images/case240/output.jpg) | GPT Image 20提示词｜极光穹顶下的360北极黑沙海岸全景 | GPT Image | 2026-06-11 | [JSON](prompts/case240.json) |
| ![case241](images/case241/output.jpg) | GPT Image 20提示词：星空露营地360沉浸式全景夜景 | GPT Image | 2026-06-10 | [JSON](prompts/case241.json) |
| ![case242](images/case242/output.jpg) | GPT Image 20提示词：银河星空下的360森林露营秘境 | GPT Image | 2026-06-10 | [JSON](prompts/case242.json) |
| ![case243](images/case243/output.jpg) | GPT Image 20提示词：极光穹顶下的黑沙海岸秘境 | GPT Image | 2026-06-10 | [JSON](prompts/case243.json) |
| ![case244](images/case244/output.jpg) | GPT Image 20提示词：极光穹顶下的冰岛极地科考营地 | GPT Image | 2026-06-10 | [JSON](prompts/case244.json) |
| ![case245](images/case245/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-08 | [JSON](prompts/case245.json) |
| ![case246](images/case246/output.jpg) | GPT Image 20提示词｜侘寂北欧极简360全景空间 | GPT Image | 2026-06-08 | [JSON](prompts/case246.json) |
| ![case247](images/case247/output.jpg) | GPT Image 20提示词：现代简约书房360全景写实空间 | GPT Image | 2026-06-08 | [JSON](prompts/case247.json) |
| ![case248](images/case248/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-08 | [JSON](prompts/case248.json) |
| ![case249](images/case249/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-04 | [JSON](prompts/case249.json) |
| ![case250](images/case250/output.jpg) | GPT Image 20提示词：360航拍森林盘山公路全景 | GPT Image | 2026-06-04 | [JSON](prompts/case250.json) |
| ![case251](images/case251/output.jpg) | GPT Image 20提示词打造超写实360VR景观｜云端秘境山谷全景 | GPT Image | 2026-06-04 | [JSON](prompts/case251.json) |
| ![case252](images/case252/output.jpg) | GPT Image 20提示词｜半穹顶花岗岩巨岩与双瀑布360全景秘境 | GPT Image | 2026-06-04 | [JSON](prompts/case252.json) |
| ![case253](images/case253/output.jpg) | GPT Image 20提示词：雪境中古城360全景暮光史诗 | GPT Image | 2026-06-03 | [JSON](prompts/case253.json) |
| ![case254](images/case254/output.jpg) | GPT Image 20提示词：中世纪欧洲古镇360全景 | GPT Image | 2026-06-03 | [JSON](prompts/case254.json) |
| ![case255](images/case255/output.jpg) | GPT Image 20提示词：吴哥窟秘境360全景神庙纪实摄影 | GPT Image | 2026-06-03 | [JSON](prompts/case255.json) |
| ![case256](images/case256/output.jpg) | GPT Image 20提示词：欧洲中世纪老城360全景纪实摄影 | GPT Image | 2026-06-03 | [JSON](prompts/case256.json) |
| ![case257](images/case257/output.jpg) | GPT Image 20提示词｜山巅骑行落日秘境 | GPT Image | 2026-06-02 | [JSON](prompts/case257.json) |
| ![case258](images/case258/output.jpg) | GPT Image 20提示词｜晨曦海蚀秘境360全景 | GPT Image | 2026-06-02 | [JSON](prompts/case258.json) |
| ![case259](images/case259/output.jpg) | GPT Image 20提示词｜苍穹孤骑纪念碑谷秘境 | GPT Image | 2026-06-02 | [JSON](prompts/case259.json) |
| ![case260](images/case260/output.jpg) | GPT Image 20提示词｜荒野木屋环景史诗 | GPT Image | 2026-06-02 | [JSON](prompts/case260.json) |
| ![case261](images/case261/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-01 | [JSON](prompts/case261.json) |
| ![case262](images/case262/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-06-01 | [JSON](prompts/case262.json) |
| ![case263](images/case263/output.jpg) | 雾海森岭｜GPT Image 20提示词全景写实巨制 | GPT Image | 2026-06-01 | [JSON](prompts/case263.json) |
| ![case264](images/case264/output.jpg) | GPT Image 20提示词｜暮光雪境360全景群峰 | GPT Image | 2026-06-01 | [JSON](prompts/case264.json) |
| ![case265](images/case265/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-05-31 | [JSON](prompts/case265.json) |
| ![case266](images/case266/output.jpg) | GPT Image 20提示词：金色晨光下的东方古镇360全景 | GPT Image | 2026-05-31 | [JSON](prompts/case266.json) |
| ![case267](images/case267/output.jpg) | GPT Image 20提示词｜侘寂光影里的360地中海静谧居室 | GPT Image | 2026-05-31 | [JSON](prompts/case267.json) |
| ![case268](images/case268/output.jpg) | GPT Image 20全景提示词｜永恒环形巨石中庭 | GPT Image | 2026-05-31 | [JSON](prompts/case268.json) |
| ![case269](images/case269/output.jpg) | GPT Image 20提示词｜超高空环形泻湖360全景秘境 | GPT Image | 2026-05-30 | [JSON](prompts/case269.json) |
| ![case270](images/case270/output.jpg) | GPT Image 20提示词 | GPT Image | 2026-05-30 | [JSON](prompts/case270.json) |
| ![case271](images/case271/output.jpg) | GPT Image 20提示词｜迈阿密温伍德360涂鸦日落全景 | GPT Image | 2026-05-30 | [JSON](prompts/case271.json) |
| ![case272](images/case272/output.jpg) | 黄金决赛之夜360全景体育场GPT Image 20提示词 | GPT Image | 2026-05-30 | [JSON](prompts/case272.json) |
| ![case273](images/case273/output.jpg) | 舒适原木风全景卧室：柔和自然光影与极简美学提示词 | GPT Image | 2026-05-29 | [JSON](prompts/case273.json) |
| ![case274](images/case274/output.jpg) |  | GPT Image | 2026-05-29 | [JSON](prompts/case274.json) |
| ![case275](images/case275/output.jpg) | 深蓝北欧书房全景提示词 | GPT Image | 2026-05-29 | [JSON](prompts/case275.json) |
| ![case276](images/case276/output.jpg) | 复古现代客厅全景空间提示词 | GPT Image | 2026-05-29 | [JSON](prompts/case276.json) |
| ![case277](images/case277/output.jpg) | 雾境隧道尽头的工业孤影｜提示词 | GPT Image | 2026-05-28 | [JSON](prompts/case277.json) |
| ![case278](images/case278/output.jpg) | 晨光古城360全景提示词 | GPT Image | 2026-05-28 | [JSON](prompts/case278.json) |
| ![case279](images/case279/output.jpg) | 晨曦古城环巷全景 | GPT Image | 2026-05-28 | [JSON](prompts/case279.json) |
| ![case280](images/case280/output.jpg) | 旧城雨痕环景叙事全景提示词 | GPT Image | 2026-05-28 | [JSON](prompts/case280.json) |
| ![case281](images/case281/output.jpg) | 南欧石板古城360度全景电影感全景街景提示词 | GPT Image | 2026-05-27 | [JSON](prompts/case281.json) |
| ![case282](images/case282/output.jpg) | 暖灯石街夜景360全景提示词 | GPT Image | 2026-05-27 | [JSON](prompts/case282.json) |
| ![case283](images/case283/output.jpg) | 复古红砖街景360全景提示词 | GPT Image | 2026-05-27 | [JSON](prompts/case283.json) |
| ![case284](images/case284/output.jpg) | 潮湿旧城区暗巷360全景提示词 | GPT Image | 2026-05-27 | [JSON](prompts/case284.json) |
| ![case285](images/case285/output.jpg) | 深蓝极简环形艺术展厅全景沉浸超现实提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case285.json) |
| ![case286](images/case286/output.jpg) | 深海火山夜爆发提示词：360度火山夜全景 | GPT Image | 2026-05-26 | [JSON](prompts/case286.json) |
| ![case287](images/case287/output.jpg) | 宁静湖岸360度环景划艇暮色森林湖提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case287.json) |
| ![case288](images/case288/output.jpg) | 360度苔藓峡谷瀑布全景沉浸自然图提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case288.json) |
| ![case289](images/case289/output.jpg) | 幽静山谷竹林环形全景写实摄影秘境图提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case289.json) |
| ![case290](images/case290/output.jpg) | 幽雾白玫瑰晨露秘境｜提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case290.json) |
| ![case291](images/case291/output.jpg) | 冰岛北境苔原风暴360全景提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case291.json) |
| ![case292](images/case292/output.jpg) | 幽光秘境红杉森林360全景提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case292.json) |
| ![case293](images/case293/output.jpg) | 《雪域天穹环景长卷》360全景提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case293.json) |
| ![case294](images/case294/output.jpg) | 冰封晨曦荒野湖泊全景 | GPT Image | 2026-05-26 | [JSON](prompts/case294.json) |
| ![case295](images/case295/output.jpg) | 云雾阿尔卑斯山口全景图提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case295.json) |
| ![case296](images/case296/output.jpg) | 《寒雾峡谷瀑流环景》提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case296.json) |
| ![case297](images/case297/output.jpg) | 《赤色死海荒漠全景》提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case297.json) |
| ![case298](images/case298/output.jpg) | 云霞映野欧陆农田360全景提示词 | GPT Image | 2026-05-26 | [JSON](prompts/case298.json) |

### 景区 (75 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case013](images/case013/output.jpg) | 大西洋火山岛海岸与绿色台地村庄全景空间 | GPT Image | 2026-08-29 | [JSON](prompts/case013.json) |
| ![case014](images/case014/output.jpg) | 蓝调夜幕下的现代斜拉桥城市海湾全景空间 | GPT Image | 2026-08-29 | [JSON](prompts/case014.json) |
| ![case015](images/case015/output.jpg) | 荒野海岸边的复古混凝土旧仓库空间 | GPT Image | 2026-08-29 | [JSON](prompts/case015.json) |
| ![case016](images/case016/output.jpg) | 极境雪山环绕·高空冰雪峰群全景空间 | GPT Image | 2026-08-29 | [JSON](prompts/case016.json) |
| ![case017](images/case017/output.jpg) | 巴西白沙丘雨季泻湖·落日秘境全景空间 | GPT Image | 2026-08-29 | [JSON](prompts/case017.json) |
| ![case018](images/case018/output.jpg) | 雾海悬崖上的绿色海岸秘境 | GPT Image | 2026-08-29 | [JSON](prompts/case018.json) |
| ![case019](images/case019/output.jpg) | 海岸礁石悬崖洞穴与海湾民居全景空间 | GPT Image | 2026-08-29 | [JSON](prompts/case019.json) |
| ![case020](images/case020/output.jpg) | 粉色极光下的乡村银河之夜 | GPT Image | 2026-08-29 | [JSON](prompts/case020.json) |
| ![case021](images/case021/output.jpg) | 沙海与大洋交汇的荒野越野秘境 | GPT Image | 2026-08-29 | [JSON](prompts/case021.json) |
| ![case022](images/case022/output.jpg) | 橘红沙漠与风暴云层交织的黄昏荒原 | GPT Image | 2026-08-29 | [JSON](prompts/case022.json) |
| ![case025](images/case025/output.jpg) | 高海拔银河星空下的云雾山谷秘境 | GPT Image | 2026-08-29 | [JSON](prompts/case025.json) |
| ![case026](images/case026/output.jpg) | 落日海湾城市天际线与梦幻滨海空间 | GPT Image | 2026-08-29 | [JSON](prompts/case026.json) |
| ![case027](images/case027/output.jpg) | 藤蔓覆盖的废墟秘境｜被森林重新占据的古老建筑遗迹 | GPT Image | 2026-08-29 | [JSON](prompts/case027.json) |
| ![case028](images/case028/output.jpg) | 高山银河露营夜｜星空下的荒野帐篷全景空间 | GPT Image | 2026-08-28 | [JSON](prompts/case028.json) |
| ![case034](images/case034/output.jpg) | 暮色裂湖·紫金天际 | GPT Image | 2026-08-20 | [JSON](prompts/case034.json) |
| ![case035](images/case035/output.jpg) | 赤岩环流 · 荒漠河谷全景 | GPT Image | 2026-08-20 | [JSON](prompts/case035.json) |
| ![case036](images/case036/output.jpg) | 阴翳海崖·苍翠之境 | GPT Image | 2026-08-20 | [JSON](prompts/case036.json) |
| ![case037](images/case037/output.jpg) | 荒原金字塔：黄昏下的雅丹孤峰 | GPT Image | 2026-08-20 | [JSON](prompts/case037.json) |
| ![case038](images/case038/output.jpg) | 天镜盐湖：荒野之上的天空倒影 | GPT Image | 2026-08-19 | [JSON](prompts/case038.json) |
| ![case039](images/case039/output.jpg) | 翡翠峡湾 · 云雾深处 | GPT Image | 2026-08-19 | [JSON](prompts/case039.json) |
| ![case040](images/case040/output.jpg) | 潮汐洞穴·碧蓝海湾 | GPT Image | 2026-08-19 | [JSON](prompts/case040.json) |
| ![case041](images/case041/output.jpg) | 地中海悬崖 · 黄金落日 | GPT Image | 2026-08-19 | [JSON](prompts/case041.json) |
| ![case056](images/case056/output.jpg) | 荒原花岗岩高原的日光秘境 | GPT Image | 2026-08-12 | [JSON](prompts/case056.json) |
| ![case057](images/case057/output.jpg) | 冰川湖泊与雪山峡谷秘境全景 | GPT Image | 2026-08-12 | [JSON](prompts/case057.json) |
| ![case058](images/case058/output.jpg) | 金辉环抱的高山梯田秘境 | GPT Image | 2026-08-12 | [JSON](prompts/case058.json) |
| ![case059](images/case059/output.jpg) | 地中海蓝色秘境悬崖海湾 | GPT Image | 2026-08-12 | [JSON](prompts/case059.json) |
| ![case060](images/case060/output.jpg) | 黄金海岸海蚀奇观日落秘境 | GPT Image | 2026-08-11 | [JSON](prompts/case060.json) |
| ![case061](images/case061/output.jpg) | 极夜血红极光下的冰封湖秘境 | GPT Image | 2026-08-11 | [JSON](prompts/case061.json) |
| ![case062](images/case062/output.jpg) | 暮色红岩峡谷荒漠沉浸空间 | GPT Image | 2026-08-11 | [JSON](prompts/case062.json) |
| ![case063](images/case063/output.jpg) | 冰岛冬日海岸360全景秘境 | GPT Image | 2026-08-11 | [JSON](prompts/case063.json) |
| ![case064](images/case064/output.jpg) | 黑曜火山海岸：加拉帕戈斯熔岩生命秘境 | GPT Image | 2026-08-11 | [JSON](prompts/case064.json) |
| ![case065](images/case065/output.jpg) | 火山雨林海湾落日之境，巨柱孤峰映照热带天堂 | GPT Image | 2026-08-11 | [JSON](prompts/case065.json) |
| ![case066](images/case066/output.jpg) | 云巅秘境：高山湖泊与森林环抱的360阿尔卑斯山谷 | GPT Image | 2026-08-11 | [JSON](prompts/case066.json) |
| ![case067](images/case067/output.jpg) | 玄武岩峡谷湖泊荒原360沉浸式秘境全景 | GPT Image | 2026-08-10 | [JSON](prompts/case067.json) |
| ![case068](images/case068/output.jpg) | 秋日溪桥漫步 | GPT Image | 2026-08-10 | [JSON](prompts/case068.json) |
| ![case069](images/case069/output.jpg) | 绿野古木圣堂：沉浸式乡村教堂360全景秘境 | GPT Image | 2026-08-10 | [JSON](prompts/case069.json) |
| ![case070](images/case070/output.jpg) | 碧海云天之上的热带秘境环岛公路全景 | GPT Image | 2026-08-10 | [JSON](prompts/case070.json) |
| ![case071](images/case071/output.jpg) | 荒漠孤野中的落日余晖·360沉浸式黄昏全景 | GPT Image | 2026-08-10 | [JSON](prompts/case071.json) |
| ![case072](images/case072/output.jpg) | 站在雅丹荒谷中心，抬头就是一整片旋转银河 | GPT Image | 2026-08-10 | [JSON](prompts/case072.json) |
| ![case083](images/case083/output.jpg) | AI水彩绘梦纽约港·360游艇全景漫游 | GPT Image | 2026-07-25 | [JSON](prompts/case083.json) |
| ![case087](images/case087/output.jpg) | 4K峡湾秘境，带你进入360云雾山海世界 | GPT Image | 2026-07-24 | [JSON](prompts/case087.json) |
| ![case088](images/case088/output.jpg) | 穿越千年长城之巅，360沉浸式云海山河全景 | GPT Image | 2026-07-24 | [JSON](prompts/case088.json) |
| ![case089](images/case089/output.jpg) | 古桥藏于山水间，360沉浸河谷秘境 | GPT Image | 2026-07-24 | [JSON](prompts/case089.json) |
| ![case090](images/case090/output.jpg) | AI打造360热带秘境海岸，沉浸式探索日落海岛奇观 | GPT Image | 2026-07-24 | [JSON](prompts/case090.json) |
| ![case091](images/case091/output.jpg) | 蔚蓝秘境：热带海岛珊瑚泻湖360全景之旅AI绘画提示词 | GPT Image | 2026-07-23 | [JSON](prompts/case091.json) |
| ![case092](images/case092/output.jpg) | 云端石峰之巅：360沉浸式高山秘境AI绘画提示词 | GPT Image | 2026-07-23 | [JSON](prompts/case092.json) |
| ![case093](images/case093/output.jpg) | 赤色荒原尽头的日落奇境：360度红土天空秘境AI提示词 | GPT Image | 2026-07-23 | [JSON](prompts/case093.json) |
| ![case094](images/case094/output.jpg) | 秋日森林秘境：360度沉浸式金色落叶奇境AI绘画提示词 | GPT Image | 2026-07-23 | [JSON](prompts/case094.json) |
| ![case095](images/case095/output.jpg) | 冰雪海湾秘境：360俯瞰冬日海岸的静谧奇观 | GPT Image | 2026-07-22 | [JSON](prompts/case095.json) |
| ![case096](images/case096/output.jpg) | 穿越暮光边界：一幅360展现自然与城市共生的全景画卷 | GPT Image | 2026-07-22 | [JSON](prompts/case096.json) |
| ![case097](images/case097/output.jpg) | 360环游红岩峡谷：感受大自然雕刻出的地球奇迹 | GPT Image | 2026-07-22 | [JSON](prompts/case097.json) |
| ![case098](images/case098/output.jpg) | 太震撼了！8K全景带你穿越北美红岩峡谷，360感受荒野史诗 | GPT Image | 2026-07-22 | [JSON](prompts/case098.json) |
| ![case099](images/case099/output.jpg) | 暮色湿地镜影·枯木与云霞交织的静谧世界AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case099.json) |
| ![case100](images/case100/output.jpg) | 雪域苍穹下的高山秘境全景之旅AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case100.json) |
| ![case101](images/case101/output.jpg) | 雪域巅峰·阿尔卑斯万丈冰峰360全景AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case101.json) |
| ![case102](images/case102/output.jpg) | 阿尔卑斯融雪季高山木屋全景秘境AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case102.json) |
| ![case103](images/case103/output.jpg) | 银河雪境·高山松林360度星空秘境AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case103.json) |
| ![case104](images/case104/output.jpg) | 七彩丹霞秘境：大地调色盘360全景奇观AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case104.json) |
| ![case105](images/case105/output.jpg) | 卡帕多奇亚洞穴遗迹峡谷360黄昏全景AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case105.json) |
| ![case106](images/case106/output.jpg) | 多洛米蒂群峰之巅的高山秘境全景AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case106.json) |
| ![case107](images/case107/output.jpg) | 暮色海岸秘境：木栈道穿越翡翠浅海的日落全景AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case107.json) |
| ![case108](images/case108/output.jpg) | 阿尔卑斯山谷360盛夏全景图AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case108.json) |
| ![case109](images/case109/output.jpg) | 北欧峡湾港口夕阳邮轮全景漫游图AI绘画提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case109.json) |
| ![case110](images/case110/output.jpg) | 阿尔卑斯峡湾湖泊360全景 GPT Image 20提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case110.json) |
| ![case111](images/case111/output.jpg) | 云隙天光下的壮丽高山峡谷360全景｜GPT Image 20提示词 | GPT Image | 2026-07-21 | [JSON](prompts/case111.json) |
| ![case158](images/case158/output.jpg) | 暮光映照阿尔卑斯断崖全景史诗风光图AI绘提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case158.json) |
| ![case159](images/case159/output.jpg) | 暮光山巅长角山羊360度全景纪实摄影图AI绘画提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case159.json) |
| ![case160](images/case160/output.jpg) | 暮光金山映照群峰史诗级360全景风光摄影AI绘画提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case160.json) |
| ![case161](images/case161/output.jpg) | 日落海岸礁石草坡360度全景风光摄影AI绘画提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case161.json) |
| ![case162](images/case162/output.jpg) | 日照红山映冰湖百内三塔史诗全景奇观AI绘画提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case162.json) |
| ![case163](images/case163/output.jpg) | 落日巨岩荒漠360全景史诗风光摄影图AI绘画提示词 | GPT Image | 2026-07-04 | [JSON](prompts/case163.json) |
| ![case188](images/case188/output.jpg) | 红岩海湾全景游轮盛夏巡航纪实AI绘画提示词 | GPT Image | 2026-06-26 | [JSON](prompts/case188.json) |
| ![case189](images/case189/output.jpg) | 威尼斯运河落日全景盛景AI绘画提示词 | GPT Image | 2026-06-26 | [JSON](prompts/case189.json) |
| ![case190](images/case190/output.jpg) | 雨林秘境阶梯瀑布360全景写实AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case190.json) |
| ![case191](images/case191/output.jpg) | 暮色悬崖海岸全景小镇写实AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case191.json) |

### 街头 (25 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case133](images/case133/output.jpg) | 现代都市高楼街景360全景VR空间展示图AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case133.json) |
| ![case134](images/case134/output.jpg) | 金色夕阳映照伊斯坦布尔历史石墙全景光影AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case134.json) |
| ![case135](images/case135/output.jpg) | 地中海午后庭院360全景图AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case135.json) |
| ![case136](images/case136/output.jpg) | 午后金辉映照现代建筑360全景图AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case136.json) |
| ![case137](images/case137/output.jpg) | 夏日午后古罗马街巷360全景AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case137.json) |
| ![case138](images/case138/output.jpg) | 都市工业后巷360全景摄影图AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case138.json) |
| ![case139](images/case139/output.jpg) | 巴黎风石拱楼梯地下通道360全景AI绘画提示词 | GPT Image | 2026-07-14 | [JSON](prompts/case139.json) |
| ![case140](images/case140/output.jpg) | 暗拱红砖光影全景AI绘画提示词 | GPT Image | 2026-07-09 | [JSON](prompts/case140.json) |
| ![case141](images/case141/output.jpg) | 英伦复古贝果涂鸦街角360度全景漫游图AI绘画提示词 | GPT Image | 2026-07-09 | [JSON](prompts/case141.json) |
| ![case142](images/case142/output.jpg) | 深夜暖灯映照京都町屋360度全景漫游夜色AI绘画提示词 | GPT Image | 2026-07-08 | [JSON](prompts/case142.json) |
| ![case143](images/case143/output.jpg) | 伦敦街角咖啡馆午后英伦生活全景AI绘画提示词 | GPT Image | 2026-07-08 | [JSON](prompts/case143.json) |
| ![case144](images/case144/output.jpg) | GPTImage欧式林荫古街360全景图AI绘画提示词 | GPT Image | 2026-07-08 | [JSON](prompts/case144.json) |
| ![case145](images/case145/output.jpg) | 赛博霓虹都市豪车360全景夜景图AI绘画提示词 | GPT Image | 2026-07-07 | [JSON](prompts/case145.json) |
| ![case146](images/case146/output.jpg) | 现代几何光影建筑通廊360全景AI绘画提示词 | GPT Image | 2026-07-07 | [JSON](prompts/case146.json) |
| ![case147](images/case147/output.jpg) | 午后暖阳映照地中海复古巷弄全景漫游AI绘画提示词 | GPT Image | 2026-07-07 | [JSON](prompts/case147.json) |
| ![case148](images/case148/output.jpg) | 360度古典地下拱廊光影史诗全景摄影AI绘画提示词 | GPT Image | 2026-07-07 | [JSON](prompts/case148.json) |
| ![case149](images/case149/output.jpg) | 巴黎皇家花园午后漫游360全景纪实光影AI绘画提示词 | GPT Image | 2026-07-07 | [JSON](prompts/case149.json) |
| ![case150](images/case150/output.jpg) | 暮色樱河映城光漫步春日梦幻全景AI绘画提示词 | GPT Image | 2026-07-06 | [JSON](prompts/case150.json) |
| ![case151](images/case151/output.jpg) | 北欧古典广场与共享单车城市全景漫游纪实AI绘画提示词 | GPT Image | 2026-07-06 | [JSON](prompts/case151.json) |
| ![case152](images/case152/output.jpg) | 伦敦金融城黑色出租车360度全景街景漫游摄影AI绘画提示词 | GPT Image | 2026-07-06 | [JSON](prompts/case152.json) |
| ![case153](images/case153/output.jpg) | 深夜都市地下通道电影级360度全景光影空间纪实AI绘画提示词 | GPT Image | 2026-07-06 | [JSON](prompts/case153.json) |
| ![case154](images/case154/output.jpg) | 清晨蓝调都市几何 · 360全景慢跑空间AI绘画提示词 | GPT Image | 2026-07-05 | [JSON](prompts/case154.json) |
| ![case155](images/case155/output.jpg) | 暖阳石巷橙色单车欧式古城360全景漫游纪实摄影AI绘画提示词 | GPT Image | 2026-07-05 | [JSON](prompts/case155.json) |
| ![case156](images/case156/output.jpg) | 午后阳光下英式红砖联排住宅360全景漫游体验AI绘画提示词 | GPT Image | 2026-07-05 | [JSON](prompts/case156.json) |
| ![case157](images/case157/output.jpg) | 漫步巴黎古典街巷沉浸式360全景摄影之旅AI绘画提示词 | GPT Image | 2026-07-05 | [JSON](prompts/case157.json) |

### 客厅 (23 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case115](images/case115/output.jpg) | 现代北欧风客厅360全景沉浸式空间设计AI绘画提示词 | GPT Image | 2026-07-19 | [JSON](prompts/case115.json) |
| ![case116](images/case116/output.jpg) | 现代北欧中古原木风温馨客厅360全景空间设计AI绘画提示词 | GPT Image | 2026-07-19 | [JSON](prompts/case116.json) |
| ![case117](images/case117/output.jpg) | 现代北欧风客厅360全景VR空间设计展示AI绘画提示词 | GPT Image | 2026-07-19 | [JSON](prompts/case117.json) |
| ![case118](images/case118/output.jpg) | 现代极简开放式客餐厅360度全景空间设计AI绘画提示词 | GPT Image | 2026-07-19 | [JSON](prompts/case118.json) |
| ![case164](images/case164/output.jpg) | 现代极简静奢360全景客厅空间设计AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case164.json) |
| ![case165](images/case165/output.jpg) | 夏日暖阳复古木屋有机现代卧室全景设计赏析AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case165.json) |
| ![case166](images/case166/output.jpg) | 现代极简艺术橙调高端客厅360全景空间设计AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case166.json) |
| ![case167](images/case167/output.jpg) | 复古现代融合客厅360度全景美学空间设计AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case167.json) |
| ![case169](images/case169/output.jpg) | 午后暖阳映照复古英式古典书房全景空间漫游体验AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case169.json) |
| ![case198](images/case198/output.jpg) | 云景环城·现代光影全景开放式奢居空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case198.json) |
| ![case199](images/case199/output.jpg) | 一镜环景·森林光影现代居所提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case199.json) |
| ![case200](images/case200/output.jpg) | 阳光环绕的北欧波西米亚开放式理想居所提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case200.json) |
| ![case201](images/case201/output.jpg) | 地中海光影·360波西米亚静谧居所提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case201.json) |
| ![case202](images/case202/output.jpg) | 极简客厅全景GPTImage20提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case202.json) |
| ![case203](images/case203/output.jpg) | 蓝调都市阁楼360环幕客厅全景提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case203.json) |
| ![case204](images/case204/output.jpg) | 北欧现代360度客厅全景空间设计提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case204.json) |
| ![case205](images/case205/output.jpg) | 午后暖光下的现代奢华全景大平层空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case205.json) |
| ![case206](images/case206/output.jpg) | 云境雅居360现代轻奢全景客厅空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case206.json) |
| ![case207](images/case207/output.jpg) | 暖光环绕的现代简约全景客厅空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case207.json) |
| ![case208](images/case208/output.jpg) | 暖光环绕的现代简约全景客厅空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case208.json) |
| ![case209](images/case209/output.jpg) | 午后暖光下的侘寂原木治愈客厅全景提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case209.json) |
| ![case210](images/case210/output.jpg) | 现代简约客厅360全景自然光空间 | GPT Image | 2026-06-23 | [JSON](prompts/case210.json) |
| ![case211](images/case211/output.jpg) | 午后暖光下的现代极简全景客餐厅空间提示词 | GPT Image | 2026-06-23 | [JSON](prompts/case211.json) |

### 人物 (15 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case051](images/case051/output.jpg) | 黄昏草甸中仰望天空的自由之境 | GPT Image | 2026-08-13 | [JSON](prompts/case051.json) |
| ![case052](images/case052/output.jpg) | 西部牛仔黄昏竞技场腾跃瞬间 | GPT Image | 2026-08-13 | [JSON](prompts/case052.json) |
| ![case053](images/case053/output.jpg) | 工业风 Loft 咖啡馆里的静谧阅读时光 | GPT Image | 2026-08-13 | [JSON](prompts/case053.json) |
| ![case054](images/case054/output.jpg) | 荒野越野赛场 ATV 飞跃瞬间 | GPT Image | 2026-08-13 | [JSON](prompts/case054.json) |
| ![case055](images/case055/output.jpg) | 高山悬崖密林徒步观景沉浸空间 | GPT Image | 2026-08-13 | [JSON](prompts/case055.json) |
| ![case128](images/case128/output.jpg) | 落日余晖映海岸情侣共舞浪漫剪影全景AI绘画提示词 | GPT Image | 2026-07-16 | [JSON](prompts/case128.json) |
| ![case129](images/case129/output.jpg) | 极简工业风城市跑酷360全景空间AI绘画提示词 | GPT Image | 2026-07-16 | [JSON](prompts/case129.json) |
| ![case130](images/case130/output.jpg) | 巨浪之巅沉浸冲浪360全景震撼体验AI绘画提示词 | GPT Image | 2026-07-16 | [JSON](prompts/case130.json) |
| ![case131](images/case131/output.jpg) | 落日沙海中的孤独旅者全景探索之境AI绘画提示词 | GPT Image | 2026-07-16 | [JSON](prompts/case131.json) |
| ![case132](images/case132/output.jpg) | 暮色草原仰望归雁自由沉浸全景之境AI绘画提示词 | GPT Image | 2026-07-16 | [JSON](prompts/case132.json) |
| ![case170](images/case170/output.jpg) | 冰岛火山断崖孤影史诗级360度全景风光AI绘画提示词 | GPT Image | 2026-06-30 | [JSON](prompts/case170.json) |
| ![case171](images/case171/output.jpg) | 北欧苔原孤旅者沉浸式360度电影全景风光提示词 | GPT Image | 2026-06-30 | [JSON](prompts/case171.json) |
| ![case172](images/case172/output.jpg) | 阴云海岸少女奔跑青春纪实360全景图提示词 | GPT Image | 2026-06-30 | [JSON](prompts/case172.json) |
| ![case177](images/case177/output.jpg) | 360森林瀑布沉浸全景摄影GPT Image 20提示词 | GPT Image | 2026-06-28 | [JSON](prompts/case177.json) |
| ![case178](images/case178/output.jpg) | 海岸绅士与极简别墅全景时尚大片AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case178.json) |

### 插画 (14 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case084](images/case084/output.jpg) | AI水彩绘梦：360古典车站光影之旅 | GPT Image | 2026-07-25 | [JSON](prompts/case084.json) |
| ![case085](images/case085/output.jpg) | 提示词公开！AI生成360少年素描拼贴艺术空间 | GPT Image | 2026-07-25 | [JSON](prompts/case085.json) |
| ![case086](images/case086/output.jpg) | 工具生成 | GPT Image | 2026-07-25 | [JSON](prompts/case086.json) |
| ![case168](images/case168/output.jpg) | 暖阳复古美式客厅360度全景空间设计赏析图AI绘画提示词 | GPT Image | 2026-07-01 | [JSON](prompts/case168.json) |
| ![case173](images/case173/output.jpg) | GPT Image 20提示词｜水彩少年写生360全景图 | GPT Image | 2026-06-29 | [JSON](prompts/case173.json) |
| ![case174](images/case174/output.jpg) | GPT Image 20 水彩书房360度全景治愈插画提示词 | GPT Image | 2026-06-29 | [JSON](prompts/case174.json) |
| ![case175](images/case175/output.jpg) | 逆流滑板少女水彩全景艺术插画提示词设计 | GPT Image | 2026-06-29 | [JSON](prompts/case175.json) |
| ![case176](images/case176/output.jpg) | 复古欧街水彩全景漫游插画提示词设计赏析AI绘画提示词 | GPT Image | 2026-06-29 | [JSON](prompts/case176.json) |
| ![case179](images/case179/output.jpg) | 雾染茶庭里的全景静默写生时光AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case179.json) |
| ![case180](images/case180/output.jpg) | 玫瑰与琴声沉睡的无尽记忆乐室AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case180.json) |
| ![case181](images/case181/output.jpg) | 自由之声：水彩漫游的城市全景AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case181.json) |
| ![case182](images/case182/output.jpg) | 花海琴声里的水彩全景时光AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case182.json) |
| ![case183](images/case183/output.jpg) | 海风轻拂的水彩海岸少女全景梦境AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case183.json) |
| ![case184](images/case184/output.jpg) | 秋日树下冥想全景水彩绘卷A绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case184.json) |

### 花 (10 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case042](images/case042/output.jpg) | 粉雾花海秘境 · 沉浸式马蹄莲湿地全景空间 | GPT Image | 2026-08-15 | [JSON](prompts/case042.json) |
| ![case043](images/case043/output.jpg) | 晨雾莲境 · 水上花开的360秘境 | GPT Image | 2026-08-15 | [JSON](prompts/case043.json) |
| ![case044](images/case044/output.jpg) | 云端之下的白色波斯菊花海 | GPT Image | 2026-08-15 | [JSON](prompts/case044.json) |
| ![case045](images/case045/output.jpg) | 花海仰望 · 春日天空下的红白火焰郁金香全景世界 | GPT Image | 2026-08-15 | [JSON](prompts/case045.json) |
| ![case046](images/case046/output.jpg) | 沉浸式花海漫游｜贴近大地的粉色波斯菊梦境 | GPT Image | 2026-08-15 | [JSON](prompts/case046.json) |
| ![case123](images/case123/output.jpg) | 金色暮光映照红色罂粟花海360全景梦境AI绘画提示词 | GPT Image | 2026-07-17 | [JSON](prompts/case123.json) |
| ![case124](images/case124/output.jpg) | 晨曦沙丘花海全景漫游自然诗意空间AI绘画提示词 | GPT Image | 2026-07-17 | [JSON](prompts/case124.json) |
| ![case125](images/case125/output.jpg) | 暮光花海映金辉梦幻矢车菊全景秘境AI绘画提示词 | GPT Image | 2026-07-17 | [JSON](prompts/case125.json) |
| ![case126](images/case126/output.jpg) | 晨雾鎏金花海原野360沉浸全景风光摄影AI绘画提示词 | GPT Image | 2026-07-17 | [JSON](prompts/case126.json) |
| ![case127](images/case127/output.jpg) | 春日粉色玉兰花海360全景梦幻花园漫游AI绘画提示词 | GPT Image | 2026-07-17 | [JSON](prompts/case127.json) |

### 游戏场景 (7 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case073](images/case073/output.jpg) | 360雾中森林，戴上耳机进入这片无人秘境 | GPT Image | 2026-08-07 | [JSON](prompts/case073.json) |
| ![case074](images/case074/output.jpg) | 误入迷雾沼泽森林，探索未知湿地秘境 | GPT Image | 2026-08-07 | [JSON](prompts/case074.json) |
| ![case075](images/case075/output.jpg) | 整个牧场世界 | GPT Image | 2026-08-07 | [JSON](prompts/case075.json) |
| ![case112](images/case112/output.jpg) | 中世纪欧洲乡村古堡全景VR沉浸式田园风光AI绘画提示词 | GPT Image | 2026-07-20 | [JSON](prompts/case112.json) |
| ![case113](images/case113/output.jpg) | 迷雾密林中的遗忘哥特教堂360全景秘境AI绘画提示词 | GPT Image | 2026-07-20 | [JSON](prompts/case113.json) |
| ![case114](images/case114/output.jpg) | 仲夏暖阳下欧式乡村运河静谧全景风光图AI绘画提示词 | GPT Image | 2026-07-20 | [JSON](prompts/case114.json) |
| 无图 | 雨林深处的失落古文明石殿遗迹全景 | GPT Image | 2026-08-07 | [JSON](prompts/case457.json) |

### 科幻场景 (7 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case076](images/case076/output.jpg) | 未来机械基地 | GPT Image | 2026-08-07 | [JSON](prompts/case076.json) |
| ![case077](images/case077/output.jpg) | 提示词揭秘｜用一张全景图打开未来星际基地的大门 | GPT Image | 2026-08-06 | [JSON](prompts/case077.json) |
| ![case078](images/case078/output.jpg) | 云海之上，一座未来摩天大楼正在苏醒 | GPT Image | 2026-08-06 | [JSON](prompts/case078.json) |
| ![case079](images/case079/output.jpg) | 一座未来星际基地，360带你进入宇宙深处 | GPT Image | 2026-08-06 | [JSON](prompts/case079.json) |
| ![case080](images/case080/output.jpg) | 一条通往未来的钢铁之路 | GPT Image | 2026-08-03 | [JSON](prompts/case080.json) |
| ![case081](images/case081/output.jpg) | 的废土工业巨塔 | GPT Image | 2026-08-03 | [JSON](prompts/case081.json) |
| ![case082](images/case082/output.jpg) | 一座遗落山谷的巨型混凝土神殿，360沉浸式探索未来建筑美学 | GPT Image | 2026-08-03 | [JSON](prompts/case082.json) |

### 古建筑 (6 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case192](images/case192/output.jpg) | 晴空古阁环庭全景图卷映春山AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case192.json) |
| ![case193](images/case193/output.jpg) | 晨曦古韵映万檐 屋脊云阁环抱千年城AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case193.json) |
| ![case194](images/case194/output.jpg) | 云山佛境万象宫阙全景图AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case194.json) |
| ![case195](images/case195/output.jpg) | 烈日荒漠中的古罗马海岸水渠遗迹全景AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case195.json) |
| ![case196](images/case196/output.jpg) | 光辉遗迹之门：古罗马全景圣殿遗址纪实AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case196.json) |
| ![case197](images/case197/output.jpg) | 雨林古庙遗迹全景：失落文明与自然共生秘境AI绘画提示词 | GPT Image | 2026-06-25 | [JSON](prompts/case197.json) |

### 动物 (4 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case029](images/case029/output.jpg) | 白头海雕掠过冰雪荒原｜冬日雪山360全景空间 | GPT Image | 2026-08-24 | [JSON](prompts/case029.json) |
| ![case030](images/case030/output.jpg) | 晨雾潮汐海岸上的黑背海鸥沉浸式空间 | GPT Image | 2026-08-24 | [JSON](prompts/case030.json) |
| ![case031](images/case031/output.jpg) | 秋冬灌木丛中的乌鸫与紫红浆果自然秘境 | GPT Image | 2026-08-24 | [JSON](prompts/case031.json) |
| ![case032](images/case032/output.jpg) | 翡翠水岸上的白鹡鸰｜风化岩石与清澈绿水的360自然全景空间 | GPT Image | 2026-08-24 | [JSON](prompts/case032.json) |

### 建筑 (4 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case047](images/case047/output.jpg) | 珊瑚红现代都市建筑天际线 | GPT Image | 2026-08-14 | [JSON](prompts/case047.json) |
| ![case048](images/case048/output.jpg) | 未来极简城市天际线 | GPT Image | 2026-08-14 | [JSON](prompts/case048.json) |
| ![case049](images/case049/output.jpg) | 未来流线双塔空中中庭 | GPT Image | 2026-08-14 | [JSON](prompts/case049.json) |
| ![case050](images/case050/output.jpg) | 黑钢玻璃金融中心黄昏广场 | GPT Image | 2026-08-14 | [JSON](prompts/case050.json) |

### 瀑布 (4 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case119](images/case119/output.jpg) | 黄金时刻塞里雅兰瀑布洞穴360全景奇境AI绘画提示词 | GPT Image | 2026-07-18 | [JSON](prompts/case119.json) |
| ![case120](images/case120/output.jpg) | 暮色圣瀑映峡谷幻境全景自然风光图AI绘画提示词 | GPT Image | 2026-07-18 | [JSON](prompts/case120.json) |
| ![case121](images/case121/output.jpg) | 原始森林峡谷飞瀑环绕沉浸式VR全景秘境AI绘画提示词 | GPT Image | 2026-07-18 | [JSON](prompts/case121.json) |
| ![case122](images/case122/output.jpg) | 金色森林瀑布秘境全景VR沉浸空间探索AI绘画提示词 | GPT Image | 2026-07-18 | [JSON](prompts/case122.json) |

### 酒店 (3 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case185](images/case185/output.jpg) | 黄昏现代简约卧室360全景空间AI绘画提示词 | GPT Image | 2026-06-27 | [JSON](prompts/case185.json) |
| ![case186](images/case186/output.jpg) | 奢华度假卧室全景AI绘画提示词 | GPT Image | 2026-06-26 | [JSON](prompts/case186.json) |
| ![case187](images/case187/output.jpg) | 黄昏现代度假村360全景AI绘画提示词 | GPT Image | 2026-06-26 | [JSON](prompts/case187.json) |

### 海底世界 (2 个)

| 预览 | 标题 | 模型 | 更新时间 | Prompt |
|------|------|------|----------|--------|
| ![case023](images/case023/output.jpg) | 高海拔雪山岩石拱门秘境 | GPT Image | 2026-08-29 | [JSON](prompts/case023.json) |
| ![case024](images/case024/output.jpg) | 热带浅海珊瑚礁生态秘境 | GPT Image | 2026-08-29 | [JSON](prompts/case024.json) |

## 🔄 自动同步机制

GitHub Actions 每天北京时间 8:00 自动运行：

- 通过 WordPress REST API 拉取 diysq.com 全景分类文章
- 对比缓存，仅同步新发布或更新的内容（增量同步）
- 自动压缩预览图至 2048px JPEG
- 提交并推送到本仓库

手动触发：仓库 → Actions → Sync from DIYSQ → Run workflow

## 📄 License

MIT