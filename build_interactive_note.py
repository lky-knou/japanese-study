# -*- coding: utf-8 -*-
import json

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/dialogues.json', 'r', encoding='utf-8') as f:
    dialogues = json.load(f)

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/audio_b64.txt', 'r') as f:
    audio_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>제2과 구로몬 시장 회화문 - 인터랙티브 일본어 학습 노트</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-light: #eff6ff;
      --primary-dark: #1d4ed8;
      --ruby-color: #2563eb;
      --text-main: #1e293b;
      --text-sub: #64748b;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --highlight: #fef08a;
      --highlight-border: #facc15;
      --mire-color: #0284c7;
      --mire-bg: #e0f2fe;
      --manami-color: #059669;
      --manami-bg: #d1fae5;
      --ojisan-color: #d97706;
      --ojisan-bg: #fef3c7;
      --stage-color: #64748b;
      --stage-bg: #f1f5f9;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans KR', 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 100px;
    }}

    /* Header & Navigation */
    header.app-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      padding: 12px 20px;
    }}

    .header-inner {{
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .title-row h1 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .title-row h1 span.badge {{
      background: #e0e7ff;
      color: #3730a3;
      font-size: 0.75rem;
      padding: 2px 8px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    .controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      padding-top: 6px;
      border-top: 1px dashed var(--border);
    }}

    .tab-group, .toggle-group, .audio-quick-controls {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    button.btn {{
      font-family: inherit;
      font-size: 0.85rem;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
      font-weight: 500;
    }}

    button.btn:hover {{
      background: #f1f5f9;
      border-color: #cbd5e1;
    }}

    button.btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    button.btn-primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    button.btn-primary:hover {{
      background: var(--primary-dark);
    }}

    button.btn-sm {{
      padding: 4px 8px;
      font-size: 0.78rem;
    }}

    /* Global Audio Player Bar (Bottom Floating) */
    .audio-dock {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: #1e293b;
      color: #f8fafc;
      padding: 10px 18px;
      border-radius: 40px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.25);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 14px;
      max-width: 92%;
    }}

    .audio-dock button {{
      background: transparent;
      border: none;
      color: white;
      cursor: pointer;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      border-radius: 50%;
      transition: background 0.15s;
    }}

    .audio-dock button:hover {{
      background: rgba(255, 255, 255, 0.15);
    }}

    .audio-dock .now-playing-info {{
      font-size: 0.82rem;
      max-width: 280px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      color: #94a3b8;
    }}

    .audio-dock .now-playing-info strong {{
      color: #38bdf8;
    }}

    .audio-dock select {{
      background: #334155;
      color: white;
      border: none;
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
    }}

    /* Main Container */
    main.container {{
      max-width: 900px;
      margin: 24px auto;
      padding: 0 16px;
    }}

    /* Ruby Furigana Styling */
    ruby {{
      ruby-position: over;
      ruby-align: center;
    }}

    rt {{
      font-size: 0.58em;
      color: var(--ruby-color);
      font-weight: 600;
      line-height: 1.1;
      user-select: none;
    }}

    body.hide-ruby rt {{
      visibility: hidden;
      opacity: 0;
    }}

    body.hide-pron .sentence-pron {{
      display: none !important;
    }}

    body.hide-trans .sentence-ko {{
      display: none !important;
    }}

    /* View: Full Dialogue (Tab 1) */
    .view-content {{
      display: none;
    }}
    .view-content.active {{
      display: block;
    }}

    .dialogue-paper {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      padding: 28px 32px;
    }}

    .paper-header {{
      border-bottom: 2px solid #0f172a;
      padding-bottom: 12px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}

    .paper-header h2 {{
      font-size: 1.4rem;
      color: #0f172a;
    }}

    .paper-header .sub {{
      font-size: 0.85rem;
      color: var(--text-sub);
    }}

    .dialogue-list {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .dialogue-row {{
      display: flex;
      gap: 14px;
      align-items: flex-start;
      padding: 10px 14px;
      border-radius: 8px;
      transition: all 0.2s ease;
      cursor: pointer;
      border: 1px solid transparent;
    }}

    .dialogue-row:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
    }}

    .dialogue-row.playing {{
      background: #fef9c3;
      border-color: #facc15;
      box-shadow: 0 2px 8px rgba(234, 179, 8, 0.15);
    }}

    .play-trigger-btn {{
      background: #e2e8f0;
      border: none;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      color: #334155;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }}

    .dialogue-row:hover .play-trigger-btn,
    .play-trigger-btn:hover {{
      background: var(--primary);
      color: white;
      transform: scale(1.05);
    }}

    .dialogue-row.playing .play-trigger-btn {{
      background: #eab308;
      color: white;
    }}

    .speaker-tag {{
      width: 75px;
      flex-shrink: 0;
      font-weight: 700;
      font-size: 0.95rem;
      padding-top: 4px;
    }}

    .speaker-mire {{ color: var(--mire-color); }}
    .speaker-manami {{ color: var(--manami-color); }}
    .speaker-ojisan {{ color: var(--ojisan-color); }}
    .speaker-stage {{ color: var(--stage-color); font-weight: normal; font-style: italic; }}

    .dialogue-content {{
      flex: 1;
    }}

    .jp-line {{
      font-size: 1.12rem;
      line-height: 1.9;
      font-family: 'Noto Sans JP', sans-serif;
      color: #0f172a;
    }}

    .dialogue-row.stage-direction {{
      background: #f8fafc;
      border-left: 3px solid #94a3b8;
      font-size: 0.95rem;
      color: #64748b;
    }}

    .dialogue-row.stage-direction .jp-line {{
      font-size: 1rem;
      color: #475569;
    }}

    /* View: Detailed Analysis Cards (Tab 2) */
    .scene-divider {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 5px solid #059669;
      padding: 12px 18px;
      border-radius: 8px;
      margin: 28px 0 18px 0;
      font-weight: 700;
      color: #065f46;
      font-size: 1.1rem;
    }}

    .analysis-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 3px 10px rgba(0,0,0,0.03);
      padding: 22px 24px;
      margin-bottom: 22px;
      transition: all 0.2s ease;
      border-left: 5px solid #cbd5e1;
    }}

    .analysis-card.speaker-mire-card {{
      border-left-color: var(--mire-color);
    }}
    .analysis-card.speaker-manami-card {{
      border-left-color: var(--manami-color);
    }}
    .analysis-card.speaker-ojisan-card {{
      border-left-color: var(--ojisan-color);
    }}
    .analysis-card.speaker-stage-card {{
      border-left-color: var(--stage-color);
      background: #fafaf9;
    }}

    .analysis-card.playing {{
      border-color: #facc15;
      border-left-color: #eab308;
      background: #fefce8;
      box-shadow: 0 4px 16px rgba(234, 179, 8, 0.2);
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .card-speaker-badge {{
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .card-audio-controls {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .card-main-jp {{
      font-family: 'Noto Sans JP', sans-serif;
      font-size: 1.25rem;
      line-height: 2.1;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 8px;
    }}

    .sentence-pron {{
      font-size: 0.92rem;
      color: #d97706;
      margin-bottom: 6px;
      line-height: 1.5;
    }}

    .sentence-ko {{
      font-size: 0.98rem;
      color: #334155;
      font-weight: 500;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px dashed var(--border);
    }}

    /* 3-Column Info Grid */
    .card-info-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 14px;
      background: #f8fafc;
      padding: 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}

    @media (max-width: 768px) {{
      .card-info-grid {{
        grid-template-columns: 1fr;
      }}
      .title-row {{
        flex-direction: column;
        align-items: flex-start;
      }}
      .controls-row {{
        flex-direction: column;
        align-items: flex-start;
      }}
    }}

    .info-col h4 {{
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #475569;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 4px;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 4px;
    }}

    .info-list {{
      list-style: none;
      font-size: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .info-list li {{
      line-height: 1.45;
    }}

    .info-list strong {{
      color: #0f172a;
    }}

    /* Print Stylesheet */
    @media print {{
      header.app-header, .audio-dock, .card-audio-controls, .play-trigger-btn {{
        display: none !important;
      }}
      body {{
        background: white;
        color: black;
        padding-bottom: 0;
      }}
      .view-content {{
        display: block !important;
      }}
      .dialogue-paper {{
        border: none;
        box-shadow: none;
        padding: 0;
        page-break-after: always;
      }}
      .analysis-card {{
        page-break-inside: avoid;
        box-shadow: none;
        border: 1px solid #ccc;
        margin-bottom: 16px;
      }}
      rt {{
        color: #111 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Sticky Top Header -->
  <header class="app-header">
    <div class="header-inner">
      <div class="title-row">
        <h1>
          <span>제2과 구로몬 시장(黒門市場) 회화문</span>
          <span class="badge">인터랙티브 학습 노트</span>
        </h1>
        <div class="tab-group">
          <button class="btn btn-primary active" id="tabBtn1" onclick="switchTab('tab1')">📖 회화문 전체 원문</button>
          <button class="btn" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 집중 분석</button>
          <button class="btn" onclick="window.print()" title="PDF로 저장하거나 인쇄">🖨️ 인쇄/PDF 저장</button>
        </div>
      </div>
      <div class="controls-row">
        <div class="audio-quick-controls">
          <button class="btn btn-sm btn-primary" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체 연속 듣기</button>
          <button class="btn btn-sm" onclick="stopAudio()">⏹ 정지</button>
          <span style="font-size: 0.8rem; color: var(--text-sub); margin-left: 6px;">배속:</span>
          <button class="btn btn-sm" onclick="setSpeed(0.8)">0.8x</button>
          <button class="btn btn-sm active" id="speed10" onclick="setSpeed(1.0)">1.0x</button>
          <button class="btn btn-sm" onclick="setSpeed(1.2)">1.2x</button>
        </div>
        <div class="toggle-group">
          <button class="btn btn-sm" id="btnToggleRuby" onclick="toggleRuby()">후리가나 숨기기</button>
          <button class="btn btn-sm" id="btnTogglePron" onclick="togglePron()">발음 숨기기</button>
          <button class="btn btn-sm" id="btnToggleTrans" onclick="toggleTrans()">해석 숨기기</button>
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- TAB 1: FULL DIALOGUE (PDF 1 Page Style) -->
    <div id="tab1" class="view-content active">
      <div class="dialogue-paper">
        <div class="paper-header">
          <div>
            <h2>会話文 (제2과 회화문 원문)</h2>
            <div class="sub">문장을 클릭하거나 왼쪽 [▶] 버튼을 누르면 해당 문장 음성이 바로 재생됩니다.</div>
          </div>
        </div>

        <div class="dialogue-list">
'''

# Generate Tab 1
for d in dialogues:
    stage_cls = "stage-direction" if d["is_stage"] else ""
    spk_tag = f'<div class="speaker-tag {d["speaker_class"]}">{d["speaker"].split()[0]}</div>' if not d["is_stage"] else ''
    html_content += f'''
          <div class="dialogue-row {stage_cls}" id="row-d-{d['id']}" onclick="playSentence({d['id']}, {d['start']}, {d['end']})">
            <button class="play-trigger-btn" title="문장 듣기" onclick="event.stopPropagation(); playSentence({d['id']}, {d['start']}, {d['end']})">▶</button>
            {spk_tag}
            <div class="dialogue-content">
              <div class="jp-line">{d['jp_ruby']}</div>
            </div>
          </div>
'''

html_content += '''
        </div>
      </div>
    </div>

    <!-- TAB 2: DETAILED ANALYSIS CARDS (PDF 2~6 Page Style) -->
    <div id="tab2" class="view-content">
'''

# Generate Tab 2
current_scene = None
for d in dialogues:
    if d["scene"] != current_scene:
        current_scene = d["scene"]
        html_content += f'''
      <div class="scene-divider">
        📍 {current_scene}
      </div>
'''
    spk_card_cls = f"{d['speaker_class']}-card"
    
    # Vocab list HTML
    vocab_html = "".join([f"<li><strong>{v[0]}</strong>: {v[1]}</li>" for v in d["vocab"]]) if d["vocab"] else "<li>-</li>"
    # Grammar list HTML
    grammar_html = "".join([f"<li><strong>{g[0]}</strong>: {g[1]}</li>" for g in d["grammar"]]) if d["grammar"] else "<li>-</li>"
    # Kanji list HTML
    kanji_items = []
    for k in d["kanji"]:
        line = " ".join([part for part in k if part])
        if line:
            kanji_items.append(f"<li>{line}</li>")
    kanji_html = "".join(kanji_items) if kanji_items else "<li>-</li>"

    html_content += f'''
      <div class="analysis-card {spk_card_cls}" id="card-d-{d['id']}">
        <div class="card-top">
          <div class="card-speaker-badge {d['speaker_class']}">
            👤 {d['speaker']}
          </div>
          <div class="card-audio-controls">
            <button class="btn btn-sm btn-primary" onclick="playSentence({d['id']}, {d['start']}, {d['end']})">▶ 1회 듣기</button>
            <button class="btn btn-sm" id="repeat-btn-{d['id']}" onclick="toggleRepeatSentence({d['id']}, {d['start']}, {d['end']})">🔁 3회 반복</button>
          </div>
        </div>

        <div class="card-main-jp" onclick="playSentence({d['id']}, {d['start']}, {d['end']})" style="cursor: pointer;" title="클릭하여 듣기">
          {d['jp_ruby']}
        </div>

        <div class="sentence-pron">[발음] {d['pron']}</div>
        <div class="sentence-ko">{d['ko']}</div>

        <div class="card-info-grid">
          <div class="info-col">
            <h4>📘 단어 정리</h4>
            <ul class="info-list">
              {vocab_html}
            </ul>
          </div>
          <div class="info-col">
            <h4>💡 문법 & 관용어</h4>
            <ul class="info-list">
              {grammar_html}
            </ul>
          </div>
          <div class="info-col">
            <h4>✍️ 한자 음과 뜻</h4>
            <ul class="info-list">
              {kanji_html}
            </ul>
          </div>
        </div>
      </div>
'''

html_content += f'''
    </div>

  </main>

  <!-- Global Audio Player Dock (Fixed Bottom) -->
  <div class="audio-dock">
    <button id="dockPlayBtn" onclick="togglePlayAll()" title="재생/일시정지">▶</button>
    <button onclick="stopAudio()" title="정지">⏹</button>
    <div class="now-playing-info" id="dockInfo">
      선택된 문장 재생 대기중
    </div>
    <select id="dockSpeed" onchange="setSpeed(parseFloat(this.value))">
      <option value="0.8">0.8x</option>
      <option value="1.0" selected>1.0x</option>
      <option value="1.2">1.2x</option>
      <option value="1.5">1.5x</option>
    </select>
  </div>

  <!-- Audio Element with Embedded Base64 -->
  <audio id="mainAudio" preload="auto">
    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    <source src="audio.mp3" type="audio/mp3">
  </audio>

  <script>
    const dialogues = {json.dumps(dialogues, ensure_ascii=False)};
    const audio = document.getElementById('mainAudio');
    const dockInfo = document.getElementById('dockInfo');
    const dockPlayBtn = document.getElementById('dockPlayBtn');
    const btnPlayAll = document.getElementById('btnPlayAll');

    let isPlayingAll = false;
    let currentSentenceId = null;
    let sentenceTimeout = null;
    let repeatCount = 0;
    let maxRepeats = 1;

    // Tab Switching
    function switchTab(tabId) {{
      document.querySelectorAll('.view-content').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      document.getElementById('tabBtn1').classList.toggle('active', tabId === 'tab1');
      document.getElementById('tabBtn2').classList.toggle('active', tabId === 'tab2');
    }}

    // Play Sentence segment
    function playSentence(id, start, end) {{
      stopAudio();
      currentSentenceId = id;
      const d = dialogues.find(x => x.id === id);
      highlightSentence(id);
      
      dockInfo.innerHTML = `<strong>${{d.speaker}}</strong>: ${{d.jp_plain}}`;
      dockPlayBtn.innerText = '⏸';

      audio.currentTime = start;
      audio.play();

      const duration = (end - start) * 1000 / audio.playbackRate;
      sentenceTimeout = setTimeout(() => {{
        if (maxRepeats > 1 && repeatCount < maxRepeats - 1) {{
          repeatCount++;
          playSentence(id, start, end);
        }} else {{
          audio.pause();
          stopHighlight();
          dockPlayBtn.innerText = '▶';
          dockInfo.innerText = '재생 완료';
          repeatCount = 0;
          maxRepeats = 1;
        }}
      }}, duration);
    }}

    // Toggle 3x Repeat
    function toggleRepeatSentence(id, start, end) {{
      maxRepeats = 3;
      repeatCount = 0;
      playSentence(id, start, end);
    }}

    // Play All sequentially
    function togglePlayAll() {{
      if (isPlayingAll) {{
        audio.pause();
        isPlayingAll = false;
        dockPlayBtn.innerText = '▶';
        btnPlayAll.innerText = '▶ 전체 연속 듣기';
        dockInfo.innerText = '일시 정지됨';
      }} else {{
        stopAudio();
        isPlayingAll = true;
        dockPlayBtn.innerText = '⏸';
        btnPlayAll.innerText = '⏸ 일시 정지';
        dockInfo.innerText = '전체 연속 재생 중...';
        audio.currentTime = 0;
        audio.play();
      }}
    }}

    // Audio timeupdate to highlight current sentence during PlayAll
    audio.addEventListener('timeupdate', () => {{
      if (isPlayingAll) {{
        const cur = audio.currentTime;
        const currentD = dialogues.find(d => cur >= d.start && cur < d.end);
        if (currentD && currentD.id !== currentSentenceId) {{
          currentSentenceId = currentD.id;
          highlightSentence(currentD.id);
          dockInfo.innerHTML = `<strong>${{currentD.speaker}}</strong>: ${{currentD.jp_plain}}`;
        }}
      }}
    }});

    audio.addEventListener('ended', () => {{
      stopAudio();
      dockInfo.innerText = '전체 재생 완료';
    }});

    function stopAudio() {{
      if (sentenceTimeout) {{
        clearTimeout(sentenceTimeout);
        sentenceTimeout = null;
      }}
      audio.pause();
      isPlayingAll = false;
      stopHighlight();
      dockPlayBtn.innerText = '▶';
      btnPlayAll.innerText = '▶ 전체 연속 듣기';
      currentSentenceId = null;
      repeatCount = 0;
      maxRepeats = 1;
    }}

    function highlightSentence(id) {{
      stopHighlight();
      const row = document.getElementById('row-d-' + id);
      const card = document.getElementById('card-d-' + id);
      if (row) {{
        row.classList.add('playing');
        if (document.getElementById('tab1').classList.contains('active')) {{
          row.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
      }}
      if (card) {{
        card.classList.add('playing');
        if (document.getElementById('tab2').classList.contains('active')) {{
          card.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
      }}
    }}

    function stopHighlight() {{
      document.querySelectorAll('.dialogue-row').forEach(el => el.classList.remove('playing'));
      document.querySelectorAll('.analysis-card').forEach(el => el.classList.remove('playing'));
    }}

    function setSpeed(rate) {{
      audio.playbackRate = rate;
      document.getElementById('dockSpeed').value = rate;
      document.querySelectorAll('.audio-quick-controls button').forEach(b => {{
        if (b.innerText.includes(rate + 'x')) {{
          b.classList.add('active');
        }} else if (b.innerText.includes('x')) {{
          b.classList.remove('active');
        }}
      }});
    }}

    // Study Helper Toggles
    function toggleRuby() {{
      document.body.classList.toggle('hide-ruby');
      const isHidden = document.body.classList.contains('hide-ruby');
      document.getElementById('btnToggleRuby').innerText = isHidden ? '후리가나 보이기' : '후리가나 숨기기';
    }}

    function togglePron() {{
      document.body.classList.toggle('hide-pron');
      const isHidden = document.body.classList.contains('hide-pron');
      document.getElementById('btnTogglePron').innerText = isHidden ? '발음 보이기' : '발음 숨기기';
    }}

    function toggleTrans() {{
      document.body.classList.toggle('hide-trans');
      const isHidden = document.body.classList.contains('hide-trans');
      document.getElementById('btnToggleTrans').innerText = isHidden ? '해석 보이기' : '해석 숨기기';
    }}
  </script>
</body>
</html>
'''

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully! Size:", len(html_content))
