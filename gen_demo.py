"""生成同步效果演示页 demo.html — 浅色风格，参考 awesome-gpt-image-2 库布局"""
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
    prompt_path = REPO / "prompts" / f"{cid}.json"
    prompt_data = {}
    if prompt_path.exists():
        try:
            prompt_data = json.load(open(prompt_path, "r", encoding="utf-8"))
        except:
            pass
    img_path = REPO / "images" / cid / "output.jpg"
    items.append({
        "id": cid,
        "title": item.get("title", cid),
        "model": item.get("model", "GPT Image"),
        "category": item.get("category", "未分类"),
        "image": f"images/{cid}/output.jpg" if img_path.exists() else "",
        "website_id": wid,
        "updated": item.get("website_updated_at", "")[:10],
        "prompt": prompt_data.get("prompt", {}),
    })

items.sort(key=lambda x: x["id"])
total = len(items)
with_image = sum(1 for x in items if x["image"])
structured = sum(1 for x in items if x["prompt"] and "_raw_prompt" not in x["prompt"] and isinstance(x["prompt"], dict))

# 按分类分组
by_cat = defaultdict(list)
for it in items:
    by_cat[it["category"]].append(it)

# 分类排序：有图的优先，然后按数量
cat_order = sorted(by_cat.keys(), key=lambda c: (-len(by_cat[c]), c))

# 分类 emoji
cat_emoji = {
    "景区": "🏔️", "人物": "👤", "古建筑": "🏯", "动物": "🦌",
    "旧版": "📦", "未分类": "📌",
}

def get_emoji(cat):
    return cat_emoji.get(cat, "🖼️")

# 生成 prompt 纯文本（从 JSON 转为可读文本）
def prompt_to_text(p):
    if not p or not isinstance(p, dict):
        return "(无 prompt)"
    # 原始文本格式（_raw_prompt）
    if "_raw_prompt" in p:
        return p["_raw_prompt"]
    lines = []
    for section, content in p.items():
        lines.append(f"【{section}】")
        if isinstance(content, dict):
            for k, v in content.items():
                if isinstance(v, (dict, list)):
                    lines.append(f"  {k}:")
                    if isinstance(v, dict):
                        for sk, sv in v.items():
                            lines.append(f"    - {sk}: {sv}")
                    elif isinstance(v, list):
                        for item in v:
                            if isinstance(item, dict):
                                for ik, iv in item.items():
                                    lines.append(f"    - {ik}: {iv}")
                            else:
                                lines.append(f"    - {item}")
                else:
                    lines.append(f"  {k}: {v}")
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    for ik, iv in item.items():
                        lines.append(f"  - {ik}: {iv}")
                else:
                    lines.append(f"  - {item}")
        else:
            lines.append(f"  {content}")
        lines.append("")
    return "\n".join(lines).strip()

# 为每个条目预生成 prompt 文本
for it in items:
    it["prompt_text"] = prompt_to_text(it["prompt"])
    if it["prompt"] and "_raw_prompt" in it["prompt"]:
        it["prompt_json"] = it["prompt"]["_raw_prompt"]
        it["is_raw"] = True
    else:
        it["prompt_json"] = json.dumps(it["prompt"], ensure_ascii=False, indent=2)
        it["is_raw"] = False

items_json = json.dumps(items, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Awesome 360° Panorama Prompts — 同步效果演示</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  background: #ffffff;
  color: #1f2328;
  line-height: 1.6;
}}
.container {{ max-width: 1080px; margin: 0 auto; padding: 0 24px; }}

/* Hero 区域 */
.hero {{
  padding: 48px 0 36px; text-align: center;
  background: linear-gradient(180deg, #f6f8fa 0%, #ffffff 100%);
  border-bottom: 1px solid #eaeef2;
}}
.hero h1 {{
  font-size: 2.4em; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.5px;
}}
.hero h1 .accent {{
  background: linear-gradient(135deg, #0969da 0%, #8250df 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}}
.hero .subtitle {{ color: #656d76; font-size: 1em; margin-bottom: 24px; max-width: 640px; margin-left: auto; margin-right: auto; }}
.hero-stats {{ display: flex; align-items: baseline; justify-content: center; gap: 12px; margin-bottom: 20px; }}
.hero-num {{
  font-size: 3.2em; font-weight: 800; letter-spacing: -2px; line-height: 1;
  background: linear-gradient(135deg, #0969da 0%, #8250df 50%, #f778ba 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}}
.hero-num-label {{ color: #656d76; font-size: 1.1em; font-weight: 500; }}
.badges {{ display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }}
.badge {{
  display: inline-flex; align-items: center; gap: 4px;
  padding: 5px 14px; border-radius: 20px; font-size: 0.82em; font-weight: 600;
  border: 1px solid #d0d7de; background: #fff; color: #1f2328;
}}
.badge.blue {{ background: #ddf4ff; border-color: #54aeff; color: #0969da; }}
.badge.green {{ background: #dafbe1; border-color: #3fb950; color: #1a7f37; }}
.badge.purple {{ background: #fbefff; border-color: #d8a9ff; color: #8250df; }}
.badge.orange {{ background: #fff8c5; border-color: #d4a72c; color: #9a6700; }}

/* 工具栏 */
.toolbar {{ display:flex; gap:10px; margin:24px 0 16px; flex-wrap:wrap; align-items:center; position:sticky; top:0; background:#fff; padding:12px 0; z-index:10; border-bottom:1px solid #eaeef2; }}
.toolbar input {{ flex:1; min-width:200px; padding:8px 12px; border:1px solid #d0d7de; border-radius:6px; font-size:0.9em; background:#fff; }}
.toolbar input:focus {{ outline:none; border-color:#0969da; box-shadow:0 0 0 3px rgba(9,105,218,.15); }}
.toolbar select {{ padding:8px 12px; border:1px solid #d0d7de; border-radius:6px; font-size:0.9em; background:#fff; }}
.view-toggle {{ display:flex; gap:0; }}
.view-btn {{ padding:7px 14px; border:1px solid #d0d7de; background:#f6f8fa; color:#656d76; cursor:pointer; font-size:0.88em; }}
.view-btn:first-child {{ border-radius:6px 0 0 6px; }}
.view-btn:last-child {{ border-radius:0 6px 6px 0; }}
.view-btn.active {{ background:#0969da; color:#fff; border-color:#0969da; }}

/* 分类导航 */
.cat-nav {{ display:flex; gap:6px; flex-wrap:wrap; margin-bottom:24px; }}
.cat-nav a {{
  padding:5px 12px; border-radius:16px; font-size:0.85em; text-decoration:none;
  background:#f6f8fa; border:1px solid #d0d7de; color:#1f2328;
}}
.cat-nav a:hover {{ background:#ddf4ff; border-color:#54aeff; color:#0969da; }}
.cat-nav a .cnt {{ color:#656d76; font-size:0.9em; }}

/* 分类区块 */
.cat-section {{ margin-bottom:36px; }}
.cat-section > h2 {{
  font-size:1.25em; padding-bottom:8px; border-bottom:2px solid #0969da;
  margin-bottom:16px; display:flex; align-items:center; gap:8px;
}}
.cat-section > h2 .cnt {{ font-size:0.7em; color:#656d76; font-weight:400; }}

/* 案例卡片 */
.case {{ border:1px solid #d0d7de; border-radius:10px; margin-bottom:16px; overflow:hidden; background:#fff; }}
.case-header {{ padding:14px 18px; background:#f6f8fa; border-bottom:1px solid #d0d7de; display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; }}
.case-header h3 {{ font-size:1em; color:#1f2328; }}
.case-header h3 .cid {{ color:#0969da; font-family:monospace; font-size:0.9em; margin-right:8px; }}
.case-tags {{ display:flex; gap:6px; }}
.case-tags span {{ padding:2px 8px; border-radius:4px; font-size:0.78em; font-weight:600; }}
.tag-model {{ background:#ddf4ff; color:#0969da; }}
.tag-cat {{ background:#fbefff; color:#8250df; }}
.case-body {{ padding:16px 18px; display:flex; gap:18px; align-items:flex-start; }}
.case-img {{ flex:0 0 42%; text-align:center; }}
.case-img img {{ width:100%; border-radius:8px; border:1px solid #d0d7de; }}
.case-img .no-img {{ padding:40px; color:#8c959f; background:#f6f8fa; border-radius:8px; font-size:0.9em; }}
.case-prompt {{ flex:1; min-width:0; }}
.case-prompt .prompt-head {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }}
.case-prompt .prompt-head span {{ font-size:0.85em; color:#656d76; font-weight:600; }}
.copy-btn {{ padding:4px 10px; border:1px solid #d0d7de; border-radius:5px; background:#fff; color:#0969da; cursor:pointer; font-size:0.8em; font-weight:600; }}
.copy-btn:hover {{ background:#ddf4ff; }}
.case-prompt pre {{
  background:#f6f8fa; border:1px solid #d0d7de; border-radius:8px;
  padding:14px; overflow-x:auto; font-size:0.78em; line-height:1.5;
  font-family:'Cascadia Code', Consolas, 'Courier New', monospace;
  white-space:pre-wrap; word-break:break-word; max-height:320px; overflow-y:auto; margin:0;
}}
.case-prompt .tabs {{ display:flex; gap:4px; margin-bottom:8px; }}
.case-prompt .tab {{ padding:4px 10px; border-radius:4px; font-size:0.8em; cursor:pointer; border:1px solid #d0d7de; background:#fff; }}
.case-prompt .tab.active {{ background:#0969da; color:#fff; border-color:#0969da; }}

/* 列表视图 */
.gallery-view {{ display:none; }}
.list-view {{ display:none; }}
.list-view.active {{ display:block; }}
.gallery-view.active {{ display:block; }}
table {{ width:100%; border-collapse:collapse; border:1px solid #d0d7de; border-radius:10px; overflow:hidden; }}
th, td {{ padding:10px 14px; text-align:left; border-bottom:1px solid #eaeef2; font-size:0.9em; }}
th {{ background:#f6f8fa; color:#656d76; font-weight:600; font-size:0.85em; }}
tr {{ cursor:pointer; }}
tr:hover {{ background:#f6f8fa; }}
td code {{ background:#f6f8fa; padding:2px 6px; border-radius:4px; font-size:0.85em; color:#0969da; }}

/* 弹窗 */
.modal {{ display:none; position:fixed; inset:0; background:rgba(0,0,0,.4); z-index:100; align-items:center; justify-content:center; padding:20px; }}
.modal.active {{ display:flex; }}
.modal-content {{ background:#fff; border:1px solid #d0d7de; border-radius:12px; max-width:800px; width:100%; max-height:88vh; overflow-y:auto; box-shadow:0 8px 32px rgba(0,0,0,.15); }}
.modal-header {{ padding:18px 22px; border-bottom:1px solid #d0d7de; display:flex; justify-content:space-between; align-items:flex-start; }}
.modal-header h2 {{ font-size:1.15em; color:#1f2328; }}
.modal-close {{ background:none; border:none; color:#656d76; font-size:1.4em; cursor:pointer; line-height:1; }}
.modal-close:hover {{ color:#1f2328; }}
.modal-body {{ padding:18px 22px; }}
.modal-body img {{ width:100%; border-radius:8px; margin-bottom:14px; border:1px solid #d0d7de; }}
.modal-meta {{ display:flex; gap:8px; margin-bottom:14px; flex-wrap:wrap; }}
.modal-meta span {{ padding:3px 10px; border-radius:5px; font-size:0.82em; font-weight:600; }}
.modal-body pre {{ background:#f6f8fa; border:1px solid #d0d7de; border-radius:8px; padding:14px; font-size:0.8em; overflow-x:auto; white-space:pre-wrap; word-break:break-word; max-height:350px; overflow-y:auto; }}

.footer {{ text-align:center; padding:28px; color:#656d76; font-size:0.85em; border-top:1px solid #d0d7de; margin-top:40px; }}
</style>
</head>
<body>
<div class="container">

  <div class="hero">
    <h1>🌍 Awesome 360° <span class="accent">Panorama Prompts</span></h1>
    <div class="subtitle">最大的开源全景图提示词库 · 每条包含完整结构化 JSON，可直接用于 GPT Image 等模型生成无缝拼接的 360° 全景图</div>
    <div class="hero-stats">
      <span class="hero-num">{total}</span>
      <span class="hero-num-label">360° 全景提示词</span>
    </div>
    <div class="badges">
      <span class="badge blue">🤖 GPT Image</span>
      <span class="badge green">🥽 VR Ready</span>
      <span class="badge purple">📄 JSON Format</span>
      <span class="badge orange">🌐 Equirectangular</span>
    </div>
  </div>

  <div class="toolbar">
    <input type="text" id="search" placeholder="🔍 搜索标题、分类、模型..." oninput="filterItems()">
    <select id="catFilter" onchange="filterItems()">
      <option value="">全部分类</option>
    </select>
    <div class="view-toggle">
      <button class="view-btn active" onclick="switchView('gallery')">卡片视图</button>
      <button class="view-btn" onclick="switchView('list')">列表视图</button>
    </div>
  </div>

  <div class="cat-nav" id="catNav"></div>

  <div class="gallery-view active" id="gallery"></div>
  <div class="list-view" id="listView">
    <table>
      <thead><tr><th>ID</th><th>标题</th><th>模型</th><th>分类</th><th>更新</th><th>图</th></tr></thead>
      <tbody id="listBody"></tbody>
    </table>
  </div>

</div>

<div class="modal" id="modal" onclick="if(event.target===this)closeModal()">
  <div class="modal-content">
    <div class="modal-header">
      <h2 id="modalTitle"></h2>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <img id="modalImg" src="" style="display:none">
      <div class="modal-meta" id="modalMeta"></div>
      <h3 style="font-size:1em;margin-bottom:8px;color:#1f2328;">📝 Prompt</h3>
      <pre id="modalJson"></pre>
    </div>
  </div>
</div>

<div class="footer">
  🌍 Awesome 360° Panorama Prompts · 最大的开源全景图提示词库
</div>

<script>
const DATA = {items_json};
const byCat = {{}};
DATA.forEach(it => {{ if(!byCat[it.category]) byCat[it.category]=[]; byCat[it.category].push(it); }});

function renderCatNav() {{
  const nav = document.getElementById('catNav');
  const cats = Object.keys(byCat).sort((a,b) => byCat[b].length - byCat[a].length);
  nav.innerHTML = cats.map(c =>
    `<a href="#cat-${{c}}">${{getEmoji(c)}} ${{c}} <span class="cnt">(${{byCat[c].length}})</span></a>`
  ).join('');
}}

function getEmoji(c) {{
  const m = {{"景区":"🏔️","人物":"👤","古建筑":"🏯","动物":"🦌","旧版":"📦","未分类":"📌"}};
  return m[c] || "🖼️";
}}

function renderGallery(items) {{
  const g = document.getElementById('gallery');
  const cats = [...new Set(items.map(x=>x.category))].sort((a,b)=>{{
    const la=items.filter(x=>x.category===a).length, lb=items.filter(x=>x.category===b).length;
    return lb-la;
  }});
  g.innerHTML = cats.map(cat => {{
    const list = items.filter(x=>x.category===cat);
    return `<div class="cat-section" id="cat-${{cat}}">
      <h2>${{getEmoji(cat)}} ${{cat}} <span class="cnt">(${{list.length}} 个案例)</span></h2>
      ${{list.map(it => `
      <div class="case">
        <div class="case-header">
          <h3><span class="cid">${{it.id}}</span>${{it.title}}</h3>
          <div class="case-tags">
            <span class="tag-model">${{it.model}}</span>
            ${{it.category ? `<span class="tag-cat">${{it.category}}</span>` : ''}}
            ${{it.is_raw ? '<span style="background:#fff8c5;color:#9a6700;">原始文本</span>' : '<span style="background:#dafbe1;color:#1a7f37;">结构化</span>'}}
          </div>
        </div>
        <div class="case-body">
          <div class="case-img">
            ${{it.image ? `<img src="${{it.image}}" alt="${{it.title}}" loading="lazy">` : '<div class="no-img">暂无预览图</div>'}}
          </div>
          <div class="case-prompt">
            <div class="prompt-head">
              <span>📝 Prompt JSON</span>
              <button class="copy-btn" onclick="copyPrompt('${{it.id}}', this)">复制</button>
            </div>
            <pre id="pre-${{it.id}}">${{escapeHtml(it.prompt_json)}}</pre>
          </div>
        </div>
      </div>`).join('')}}
    </div>`;
  }}).join('');
}}

function renderList(items) {{
  const tb = document.getElementById('listBody');
  tb.innerHTML = items.map(it => `
    <tr onclick="openModal('${{it.id}}')">
      <td><code>${{it.id}}</code></td>
      <td>${{it.title}}</td>
      <td><span class="tag-model" style="padding:2px 8px;border-radius:4px;font-size:.8em;background:#ddf4ff;color:#0969da;">${{it.model}}</span></td>
      <td>${{it.category || '-'}}</td>
      <td>${{it.updated || '-'}}</td>
      <td>${{it.image ? '🖼️' : '-'}}</td>
    </tr>
  `).join('');
}}

function copyPrompt(id, btn) {{
  const text = document.getElementById('pre-'+id).textContent;
  navigator.clipboard.writeText(text).then(() => {{
    btn.textContent = '已复制 ✓';
    setTimeout(() => btn.textContent = '复制', 1500);
  }});
}}

function escapeHtml(s) {{
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}}

function initFilters() {{
  const cats = [...new Set(DATA.map(x=>x.category).filter(Boolean))].sort();
  const sel = document.getElementById('catFilter');
  cats.forEach(c => {{ const o=document.createElement('option'); o.value=c; o.textContent=c; sel.appendChild(o); }});
}}

function filterItems() {{
  const q = document.getElementById('search').value.toLowerCase();
  const cat = document.getElementById('catFilter').value;
  const filtered = DATA.filter(it =>
    (!cat || it.category===cat) &&
    (!q || it.title.toLowerCase().includes(q) || it.model.toLowerCase().includes(q) || (it.category||'').toLowerCase().includes(q))
  );
  renderGallery(filtered);
  renderList(filtered);
}}

function switchView(view) {{
  document.querySelectorAll('.view-btn').forEach((b,i)=>b.classList.toggle('active', (view==='gallery')===(i===0)));
  document.querySelector('.gallery-view').classList.toggle('active', view==='gallery');
  document.querySelector('.list-view').classList.toggle('active', view==='list');
}}

function openModal(id) {{
  const it = DATA.find(x=>x.id===id);
  if(!it) return;
  document.getElementById('modalTitle').textContent = it.id + ' · ' + it.title;
  const img = document.getElementById('modalImg');
  if(it.image) {{ img.src=it.image; img.style.display='block'; }} else {{ img.style.display='none'; }}
  document.getElementById('modalMeta').innerHTML = `
    <span style="background:#ddf4ff;color:#0969da;">${{it.model}}</span>
    ${{it.category?`<span style="background:#fbefff;color:#8250df;">${{it.category}}</span>`:''}}
    ${{it.updated?`<span style="background:#f6f8fa;color:#656d76;border:1px solid #d0d7de;">更新: ${{it.updated}}</span>`:''}}
  `;
  document.getElementById('modalJson').textContent = it.prompt_json;
  document.getElementById('modal').classList.add('active');
  document.body.style.overflow='hidden';
}}

function closeModal() {{
  document.getElementById('modal').classList.remove('active');
  document.body.style.overflow='';
}}

document.addEventListener('keydown', e=>{{ if(e.key==='Escape') closeModal(); }});
initFilters();
renderCatNav();
renderGallery(DATA);
renderList(DATA);
</script>
</body>
</html>"""

out = REPO / "demo.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"演示页已生成: {out}")
print(f"共 {total} 条，{with_image} 条含图，{len(cat_order)} 个分类")
