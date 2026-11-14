# -*- coding: utf-8 -*-
import json
import subprocess
import os

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/dialogues.json', 'r', encoding='utf-8') as f:
    dialogues = json.load(f)

# Page 1: Dialogue Full Overview
scene1_items = [d for d in dialogues if '장면 1' in str(d['scene'])]
scene2_items = [d for d in dialogues if '장면 2' in str(d['scene'])]

def render_dialogue_list(items):
    html = []
    for d in items:
        if d['is_stage']:
            html.append(f'''
            <div class="p1-row stage">
              <span class="p1-text">{d['jp_ruby']}</span>
            </div>
            ''')
        else:
            spk = d['speaker'].split()[0]
            spk_class = d['speaker_class']
            html.append(f'''
            <div class="p1-row">
              <span class="p1-speaker {spk_class}">{spk}</span>
              <span class="p1-text">{d['jp_ruby']}</span>
            </div>
            ''')
    return "\n".join(html)

scene1_html = render_dialogue_list(scene1_items)
scene2_html = render_dialogue_list(scene2_items)

# Pages 2+: Detailed Sentence Breakdown
analysis_html = []
current_scene = None

for d in dialogues:
    if d['scene'] != current_scene:
        current_scene = d['scene']
        analysis_html.append(f'''
        <div class="section-title">
          📍 {current_scene}
        </div>
        ''')

    spk_title = f"👤 {d['speaker']}" if d['is_stage'] else f"🗣️ {d['speaker']}"

    vocab_list = "".join([f"<li><strong>{v[0]}</strong>: {v[1]}</li>" for v in d.get('vocab', [])])
    grammar_list = "".join([f"<li><strong>{g[0]}</strong>: {g[1]}</li>" for g in d.get('grammar', [])])
    
    kanji_items = []
    for k_pair in d.get('kanji', []):
        pair_str = " &nbsp;&nbsp; ".join([k for k in k_pair if k])
        if pair_str:
            kanji_items.append(f"<li>{pair_str}</li>")
    kanji_html = "".join(kanji_items) if kanji_items else "<li>(해당 없음)</li>"

    analysis_html.append(f'''
    <div class="pdf-card {d['speaker_class']}-border">
      <div class="card-head">
        <span class="badge-num">[문장 {d['id']:02d}]</span>
        <span class="badge-speaker {d['speaker_class']}">{spk_title}</span>
      </div>

      <div class="card-jp">
        {d['jp_ruby']}
      </div>

      <div class="card-pron">{d['pron']}</div>
      <div class="card-ko">{d['ko']}</div>

      <div class="card-boxes">
        <div class="box box-vocab">
          <div class="box-title">📘 단어 정리</div>
          <ul>{vocab_list}</ul>
        </div>
        <div class="box box-grammar">
          <div class="box-title">💡 문법 & 관용어</div>
          <ul>{grammar_list}</ul>
        </div>
        <div class="box box-kanji">
          <div class="box-title">✍️ 한자 음과 뜻</div>
          <ul>{kanji_html}</ul>
        </div>
      </div>
    </div>
    ''')

analysis_content = "\n".join(analysis_html)

html_template = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>제2과 구로몬 시장 회화문 학습 노트</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4;
      margin: 12mm 14mm 12mm 14mm;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans KR', 'Noto Sans JP', sans-serif;
      color: #0f172a;
      background: #ffffff;
      line-height: 1.5;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    /* 1페이지: 전체 회화문 */
    .page-1 {{
      page-break-after: always;
      break-after: page;
    }}

    .doc-header {{
      border-bottom: 2px solid #2563eb;
      padding-bottom: 6px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}

    .doc-title h1 {{
      font-size: 18pt;
      font-weight: 700;
      color: #1e3a8a;
      letter-spacing: -0.5px;
    }}

    .doc-title p {{
      font-size: 9pt;
      color: #475569;
      margin-top: 2px;
    }}

    .doc-meta {{
      font-size: 8.5pt;
      color: #64748b;
      text-align: right;
    }}

    .p1-scene-title {{
      background: #f0fdf4;
      color: #166534;
      border-left: 4px solid #22c55e;
      padding: 4px 8px;
      font-weight: 700;
      font-size: 10pt;
      margin: 10px 0 6px;
      border-radius: 2px;
    }}

    .p1-dialogue-list {{
      margin-bottom: 6px;
    }}

    .p1-row {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 4px 4px;
      border-bottom: 1px solid #f1f5f9;
      font-size: 10.5pt;
      line-height: 2.0;
    }}

    .p1-row.stage {{
      background: #fafaf9;
      color: #475569;
      border-radius: 3px;
      padding-left: 6px;
    }}

    .p1-speaker {{
      width: 50px;
      font-weight: 700;
      flex-shrink: 0;
    }}

    .speaker-mire {{ color: #0284c7; }}
    .speaker-manami {{ color: #059669; }}
    .speaker-ojisan {{ color: #d97706; }}
    .speaker-stage {{ color: #64748b; }}

    .p1-text {{
      flex: 1;
      font-family: 'Noto Sans JP', sans-serif;
    }}

    ruby {{
      ruby-align: center;
    }}
    rt {{
      font-size: 0.6em;
      color: #1d4ed8;
      font-weight: 700;
    }}

    /* 2페이지부터: 문장별 심층 분석 */
    .section-title {{
      background: #eff6ff;
      color: #1e40af;
      border-left: 4px solid #3b82f6;
      padding: 5px 10px;
      font-weight: 700;
      font-size: 10.5pt;
      margin: 12px 0 8px;
      border-radius: 3px;
    }}

    .pdf-card {{
      border: 1px solid #cbd5e1;
      border-left: 4px solid #94a3b8;
      border-radius: 5px;
      padding: 9px 12px;
      margin-bottom: 11px;
      background: #ffffff;
      break-inside: avoid;
      page-break-inside: avoid;
    }}

    .speaker-mire-border {{ border-left-color: #0284c7 !important; }}
    .speaker-manami-border {{ border-left-color: #059669 !important; }}
    .speaker-ojisan-border {{ border-left-color: #d97706 !important; }}
    .speaker-stage-border {{ border-left-color: #64748b !important; background: #fafaf9 !important; }}

    .card-head {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
      border-bottom: 1px dashed #e2e8f0;
      padding-bottom: 3px;
    }}

    .badge-num {{
      font-size: 8.5pt;
      font-weight: 700;
      background: #f1f5f9;
      color: #475569;
      padding: 1px 6px;
      border-radius: 3px;
    }}

    .badge-speaker {{
      font-size: 9.5pt;
      font-weight: 700;
    }}

    .card-jp {{
      font-family: 'Noto Sans JP', sans-serif;
      font-size: 12pt;
      font-weight: 500;
      line-height: 2.1;
      color: #0f172a;
      margin-bottom: 3px;
    }}

    .card-pron {{
      font-size: 8.8pt;
      color: #d97706;
      margin-bottom: 3px;
      line-height: 1.35;
    }}

    .card-ko {{
      font-size: 9.2pt;
      color: #334155;
      font-weight: 500;
      margin-bottom: 6px;
      line-height: 1.35;
    }}

    .card-boxes {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
      margin-top: 5px;
    }}

    .box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 5px 8px;
    }}

    .box-kanji {{
      grid-column: span 2;
    }}

    .box-title {{
      font-size: 8.5pt;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 3px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 2px;
    }}

    .box ul {{
      list-style: none;
      padding-left: 0;
    }}

    .box li {{
      font-size: 8pt;
      line-height: 1.45;
      color: #334155;
      margin-bottom: 2px;
      border-bottom: 1px dotted #f1f5f9;
      padding-bottom: 2px;
    }}
    .box li:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}
    .box strong {{
      color: #0f172a;
    }}
  </style>
</head>
<body>

  <!-- 1페이지: 전체 회화문 원문 (한눈에 보는 대화 전체) -->
  <section class="page-1">
    <header class="doc-header">
      <div class="doc-title">
        <h1>第2課 黒門市場 (제2과 구로몬 시장)</h1>
        <p>일본어활용1 · 회화문 원문 및 한자 후리가나(루비 문자) 완벽 조판</p>
      </div>
      <div class="doc-meta">
        <div>방송통신대학교 일본학과</div>
        <div>한국어 번역 & 어휘·문법 심층 해설본</div>
      </div>
    </header>

    <div class="p1-scene-title">📍 장면 1: 구로몬 시장 구경과 해산물 구이</div>
    <div class="p1-dialogue-list">
      {scene1_html}
    </div>

    <div class="p1-scene-title">📍 장면 2: 과일가게에서의 흥정</div>
    <div class="p1-dialogue-list">
      {scene2_html}
    </div>
  </section>

  <!-- 2페이지부터: 문장별 심층 학습 노트 -->
  <section class="page-breakdown">
    <header class="doc-header" style="margin-top: 6px;">
      <div class="doc-title">
        <h1 style="font-size: 15pt;">일본어 회화문 문장별 심층 분석 노트</h1>
        <p>어휘·품사·음편·관용구·문법 구조 및 간사이 사투리 문화 완벽 해설</p>
      </div>
      <div class="doc-meta">
        <div>第2課 黒門市場</div>
        <div>19개 전 문장 심층 분석</div>
      </div>
    </header>

    {analysis_content}
  </section>

</body>
</html>
'''

temp_html_path = '/tmp/lesson2_print_ready.html'
with open(temp_html_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

output_pdf_path = '/tmp/lesson2_new.pdf'

chrome_cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    f'--print-to-pdf={output_pdf_path}',
    '--no-pdf-header-footer',
    temp_html_path
]

print("Running Chrome headless to generate high quality PDF...")
res = subprocess.run(chrome_cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)

if os.path.exists(output_pdf_path):
    size = os.path.getsize(output_pdf_path)
    print(f"Generated PDF successfully! Size: {size:,} bytes")
