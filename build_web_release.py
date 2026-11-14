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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>제2과 구로몬 시장 회화문 - 인터랙티브 일본어 학습 노트</title>
  
  <!-- 카카오톡 인앱 브라우저 탈출 스크립트 (안드로이드 크롬 자동 실행) -->
  <script>
    (function() {{
      const ua = navigator.userAgent.toLowerCase();
      if (ua.indexOf('kakaotalk') > -1) {{
        if (ua.indexOf('android') > -1 && location.protocol.startsWith('http')) {{
          // 안드로이드 카카오톡: 크롬 브라우저 자동 실행
          location.href = 'intent://' + location.host + location.pathname + location.search + '#Intent;scheme=https;package=com.android.chrome;end';
        }}
      }}
    }})();
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary: #2563eb;
      --primary-light: #eff6ff;
      --primary-dark: #1d4ed8;
      --ruby-color: #1d4ed8;
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
      --font-scale: 1.0;
    }}

    body.font-large {{ --font-scale: 1.25; }}
    body.font-xlarge {{ --font-scale: 1.5; }}

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
      padding-bottom: 120px;
      -webkit-text-size-adjust: 100%;
    }}

    /* 카카오톡 안내 배너 */
    #kakaoNotice {{
      display: none;
      background: #eff6ff;
      border-bottom: 1px solid #bfdbfe;
      padding: 8px 14px;
      font-size: 0.8rem;
      color: #1e40af;
      text-align: center;
      position: sticky;
      top: 0;
      z-index: 1001;
    }}

    /* Header & Navigation */
    header.app-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      padding: 10px 16px;
    }}

    .header-inner {{
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .title-row h1 {{
      font-size: calc(1.15rem * var(--font-scale));
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .title-row h1 span.badge {{
      background: #e0e7ff;
      color: #3730a3;
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    .top-action-group {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 6px;
      border-top: 1px dashed var(--border);
    }}

    .tab-group, .toggle-group, .audio-quick-controls, .font-size-group {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: wrap;
    }}

    button.btn, a.btn {{
      font-family: inherit;
      font-size: 0.82rem;
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
      font-weight: 500;
      white-space: nowrap;
      text-decoration: none;
    }}

    button.btn:hover, a.btn:hover {{
      background: #f1f5f9;
      border-color: #cbd5e1;
    }}

    button.btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    button.btn-primary, a.btn-primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    button.btn-primary:hover, a.btn-primary:hover {{
      background: var(--primary-dark);
    }}

    button.btn-success, a.btn-success {{
      background: #059669;
      color: white;
      border-color: #059669;
    }}
    button.btn-success:hover, a.btn-success:hover {{
      background: #047857;
    }}

    button.btn-sm {{
      padding: 4px 8px;
      font-size: 0.75rem;
    }}

    /* Global Audio Player Bar (Bottom Floating) */
    .audio-dock {{
      position: fixed;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      background: #0f172a;
      color: #f8fafc;
      padding: 8px 16px;
      border-radius: 40px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 10px;
      max-width: 95%;
      border: 1px solid rgba(255,255,255,0.15);
    }}

    .audio-dock button {{
      background: transparent;
      border: none;
      color: white;
      cursor: pointer;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      border-radius: 50%;
      transition: background 0.15s;
    }}

    .audio-dock button:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .audio-dock .now-playing-info {{
      font-size: 0.8rem;
      max-width: 200px;
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
      padding: 3px 6px;
      border-radius: 6px;
      font-size: 0.75rem;
      cursor: pointer;
    }}

    /* Main Container */
    main.container {{
      max-width: 900px;
      margin: 18px auto;
      padding: 0 12px;
    }}

    /* Ruby Furigana Styling */
    ruby {{
      ruby-position: over;
      ruby-align: center;
      display: inline-ruby;
    }}

    rt {{
      font-size: 0.62em;
      color: var(--ruby-color);
      font-weight: 600;
      line-height: 1.0;
      user-select: none;
      transform: translateY(-2px);
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
      padding: 20px 22px;
    }}

    .paper-header {{
      border-bottom: 2px solid #0f172a;
      padding-bottom: 10px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}

    .paper-header h2 {{
      font-size: calc(1.3rem * var(--font-scale));
      color: #0f172a;
    }}

    .paper-header .sub {{
      font-size: 0.82rem;
      color: var(--text-sub);
    }}

    .dialogue-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .dialogue-row {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      padding: 10px 12px;
      border-radius: 8px;
      transition: all 0.2s ease;
      cursor: pointer;
      border: 1px solid transparent;
      -webkit-tap-highlight-color: rgba(37, 99, 235, 0.1);
    }}

    .dialogue-row:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
    }}

    .dialogue-row.playing {{
      background: #fef9c3;
      border-color: #facc15;
      box-shadow: 0 2px 8px rgba(234, 179, 8, 0.2);
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
      margin-top: 4px;
      transition: all 0.15s;
    }}

    .dialogue-row:hover .play-trigger-btn,
    .play-trigger-btn:hover {{
      background: var(--primary);
      color: white;
      transform: scale(1.08);
    }}

    .dialogue-row.playing .play-trigger-btn {{
      background: #eab308;
      color: white;
    }}

    .speaker-tag {{
      width: 70px;
      flex-shrink: 0;
      font-weight: 700;
      font-size: calc(0.95rem * var(--font-scale));
      padding-top: 6px;
    }}

    .speaker-mire {{ color: var(--mire-color); }}
    .speaker-manami {{ color: var(--manami-color); }}
    .speaker-ojisan {{ color: var(--ojisan-color); }}
    .speaker-stage {{ color: var(--stage-color); font-weight: normal; font-style: italic; }}

    .dialogue-content {{
      flex: 1;
    }}

    .jp-line {{
      font-size: calc(1.18rem * var(--font-scale));
      line-height: 2.1;
      font-family: 'Noto Sans JP', sans-serif;
      color: #0f172a;
      word-break: keep-all;
      overflow-wrap: break-word;
    }}

    .dialogue-row.stage-direction {{
      background: #f8fafc;
      border-left: 3px solid #94a3b8;
      padding-left: 14px;
    }}

    .dialogue-row.stage-direction .jp-line {{
      font-size: calc(1.05rem * var(--font-scale));
      color: #475569;
    }}

    /* View: Detailed Analysis Cards (Tab 2) */
    .scene-divider {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 5px solid #059669;
      padding: 10px 16px;
      border-radius: 8px;
      margin: 24px 0 16px 0;
      font-weight: 700;
      color: #065f46;
      font-size: calc(1.05rem * var(--font-scale));
    }}

    .analysis-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 3px 10px rgba(0,0,0,0.03);
      padding: 18px 20px;
      margin-bottom: 18px;
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
      margin-bottom: 10px;
    }}

    .card-speaker-badge {{
      font-weight: 700;
      font-size: calc(0.95rem * var(--font-scale));
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .card-audio-controls {{
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .card-main-jp {{
      font-family: 'Noto Sans JP', sans-serif;
      font-size: calc(1.3rem * var(--font-scale));
      line-height: 2.2;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 8px;
      word-break: keep-all;
      overflow-wrap: break-word;
    }}

    .sentence-pron {{
      font-size: calc(0.95rem * var(--font-scale));
      color: #d97706;
      margin-bottom: 6px;
      line-height: 1.5;
    }}

    .sentence-ko {{
      font-size: calc(1.02rem * var(--font-scale));
      color: #334155;
      font-weight: 500;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px dashed var(--border);
      line-height: 1.55;
    }}

    /* 3-Column Info Grid */
    .card-info-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      background: #f8fafc;
      padding: 12px;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}

    .info-col h4 {{
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #475569;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 4px;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 4px;
    }}

    .info-list {{
      list-style: none;
      font-size: calc(0.88rem * var(--font-scale));
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .info-list li {{
      line-height: 1.45;
      word-break: keep-all;
    }}

    .info-list strong {{
      color: #0f172a;
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
      .speaker-tag {{
        width: 60px;
      }}
      .dialogue-paper {{
        padding: 14px 14px;
      }}
      .audio-dock .now-playing-info {{
        max-width: 140px;
      }}
    }}

    /* Print Stylesheet */
    @media print {{
      #kakaoNotice, header.app-header, .audio-dock, .card-audio-controls, .play-trigger-btn {{
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

  <!-- 카카오톡 인앱 안내 (아이폰 등에서 필요시 표시) -->
  <div id="kakaoNotice">
    💡 소리가 안 나거나 화면이 멈추면 우측 상단 <strong>[ ⋮ ]</strong> 메뉴를 눌러 <strong>[다른 브라우저로 열기(Chrome/Safari)]</strong>를 선택해 주세요.
  </div>

  <!-- Sticky Top Header -->
  <header class="app-header">
    <div class="header-inner">
      <div class="title-row">
        <h1>
          <span>제2과 구로몬 시장(黒門市場) 회화문</span>
          <span class="badge">인터랙티브 학습 노트</span>
        </h1>
        
        <div class="top-action-group">
          <div class="tab-group">
            <button class="btn btn-primary active" id="tabBtn1" onclick="switchTab('tab1')">📖 원문 보기</button>
            <button class="btn" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 분석</button>
          </div>
          <!-- 파일 다운로드 버튼 (오프라인 소장 / PC용) -->
          <button class="btn btn-success" onclick="downloadCurrentHtml()" title="이 학습 노트를 파일로 내 컴퓨터/폰에 저장">📥 파일 다운로드</button>
          <button class="btn" onclick="window.print()" title="PDF로 저장하거나 인쇄">🖨️ PDF 인쇄</button>
        </div>
      </div>
      
      <div class="controls-row">
        <div class="audio-quick-controls">
          <button class="btn btn-sm btn-primary" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체 연속 듣기</button>
          <button class="btn btn-sm" onclick="stopAudio()">⏹ 정지</button>
          <span style="font-size: 0.75rem; color: var(--text-sub); margin-left: 4px;">배속:</span>
          <button class="btn btn-sm" onclick="setSpeed(0.8)">0.8x</button>
          <button class="btn btn-sm active" id="speed10" onclick="setSpeed(1.0)">1.0x</button>
          <button class="btn btn-sm" onclick="setSpeed(1.2)">1.2x</button>
        </div>
        
        <!-- 모바일 가독성: 글자 크기 조절 버튼 -->
        <div class="font-size-group">
          <span style="font-size: 0.75rem; color: var(--text-sub);">글자크기:</span>
          <button class="btn btn-sm active" id="fontNormalBtn" onclick="setFontScale('normal')">보통</button>
          <button class="btn btn-sm" id="fontLargeBtn" onclick="setFontScale('large')">크게</button>
          <button class="btn btn-sm" id="fontXLargeBtn" onclick="setFontScale('xlarge')">아주크게</button>
        </div>

        <div class="toggle-group">
          <button class="btn btn-sm" id="btnToggleRuby" onclick="toggleRuby()">후리가나</button>
          <button class="btn btn-sm" id="btnTogglePron" onclick="togglePron()">발음</button>
          <button class="btn btn-sm" id="btnToggleTrans" onclick="toggleTrans()">해석</button>
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- TAB 1: FULL DIALOGUE -->
    <div id="tab1" class="view-content active">
      <div class="dialogue-paper">
        <div class="paper-header">
          <div>
            <h2>会話文 (제2과 회화문 원문)</h2>
            <div class="sub">문장을 터치하거나 왼쪽 [▶] 버튼을 누르면 해당 문장 음성이 바로 재생됩니다.</div>
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

    <!-- TAB 2: DETAILED ANALYSIS CARDS -->
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
    
    vocab_html = "".join([f"<li><strong>{v[0]}</strong>: {v[1]}</li>" for v in d["vocab"]]) if d["vocab"] else "<li>-</li>"
    grammar_html = "".join([f"<li><strong>{g[0]}</strong>: {g[1]}</li>" for g in d["grammar"]]) if d["grammar"] else "<li>-</li>"
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

        <div class="card-main-jp" onclick="playSentence({d['id']}, {d['start']}, {d['end']})" style="cursor: pointer;" title="터치하여 듣기">
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

  <!-- Global Audio Player Dock -->
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

    // 모바일 터치 오디오 언락
    let audioUnlocked = false;
    function unlockAudio() {{
      if (audioUnlocked) return;
      audio.play().then(() => {{
        audio.pause();
        audio.currentTime = 0;
        audioUnlocked = true;
      }}).catch(() => {{}});
      window.removeEventListener('touchstart', unlockAudio);
      window.removeEventListener('click', unlockAudio);
    }}
    window.addEventListener('touchstart', unlockAudio, {{ once: true }});
    window.addEventListener('click', unlockAudio, {{ once: true }});

    // 파일 다운로드 기능 (현재 페이지를 오프라인용 단일 html 파일로 저장)
    function downloadCurrentHtml() {{
      const htmlText = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;
      const blob = new Blob([htmlText], {{ type: 'text/html;charset=utf-8' }});
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = '제2과_구로몬시장_인터랙티브_학습노트.html';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(link.href);
    }}

    // Font Scaling
    function setFontScale(scale) {{
      document.body.classList.remove('font-large', 'font-xlarge');
      document.getElementById('fontNormalBtn').classList.remove('active');
      document.getElementById('fontLargeBtn').classList.remove('active');
      document.getElementById('fontXLargeBtn').classList.remove('active');

      if (scale === 'large') {{
        document.body.classList.add('font-large');
        document.getElementById('fontLargeBtn').classList.add('active');
      }} else if (scale === 'xlarge') {{
        document.body.classList.add('font-xlarge');
        document.getElementById('fontXLargeBtn').classList.add('active');
      }} else {{
        document.getElementById('fontNormalBtn').classList.add('active');
      }}
    }}

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
      
      dockInfo.innerHTML = `<strong>${{d.speaker.split()[0]}}</strong>: ${{d.jp_plain}}`;
      dockPlayBtn.innerText = '⏸';

      audio.currentTime = start;
      const playPromise = audio.play();
      if (playPromise !== undefined) {{
        playPromise.catch(err => console.log('Playback error:', err));
      }}

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
        audio.play().catch(e => console.log(e));
      }}
    }}

    audio.addEventListener('timeupdate', () => {{
      if (isPlayingAll) {{
        const cur = audio.currentTime;
        const currentD = dialogues.find(d => cur >= d.start && cur < d.end);
        if (currentD && currentD.id !== currentSentenceId) {{
          currentSentenceId = currentD.id;
          highlightSentence(currentD.id);
          dockInfo.innerHTML = `<strong>${{currentD.speaker.split()[0]}}</strong>: ${{currentD.jp_plain}}`;
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
      document.getElementById('btnToggleRuby').classList.toggle('active', isHidden);
    }}

    function togglePron() {{
      document.body.classList.toggle('hide-pron');
      const isHidden = document.body.classList.contains('hide-pron');
      document.getElementById('btnTogglePron').classList.toggle('active', isHidden);
    }}

    function toggleTrans() {{
      document.body.classList.toggle('hide-trans');
      const isHidden = document.body.classList.contains('hide-trans');
      document.getElementById('btnToggleTrans').classList.toggle('active', isHidden);
    }}

    // 카카오톡 감지 시 알림 배너 표시
    if (/kakaotalk/i.test(navigator.userAgent)) {{
      const notice = document.getElementById('kakaoNotice');
      if (notice) notice.style.display = 'block';
    }}
  </script>
</body>
</html>
'''

# Update local files
paths = [
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/index.html',
    '/Users/kwangyulllee/Desktop/일본어/일본어활용1/제2과_구로몬시장_인터랙티브_학습노트.html',
    '/Users/kwangyulllee/Desktop/일본어/제2과_구로몬시장_인터랙티브_학습노트.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Generated enhanced HTML with Kakao Auto-Intent and Download Button!")
