# -*- coding: utf-8 -*-
import json
import os

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/dialogues.json', 'r', encoding='utf-8') as f:
    dialogues = json.load(f)

with open('/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/audio_b64.txt', 'r') as f:
    audio_b64 = f.read().strip()

# Generate Tab 1 (원문 보기) HTML
tab1_html = []
current_scene = None

for d in dialogues:
    if d['scene'] != current_scene:
        current_scene = d['scene']
        scene_title = "구로몬 시장 구경과 해산물 구이" if current_scene == 1 else "과일가게에서의 흥정"
        tab1_html.append(f'''
        <div class="scene-header">
          📍 장면 {current_scene}: {scene_title}
        </div>
        ''')

    if d['is_stage']:
        tab1_html.append(f'''
        <div class="dialogue-item stage-item" id="row-d-{d['id']}" onclick="toggleRowPlay({d['id']})">
          <div class="row-audio-ctrls" onclick="event.stopPropagation();">
            <button class="row-play-btn" id="row-play-btn-{d['id']}" title="재생 / 일시정지" onclick="toggleRowPlay({d['id']})">▶</button>
            <button class="row-stop-btn" id="row-stop-btn-{d['id']}" title="정지" onclick="stopSentence({d['id']})">⏹</button>
          </div>
          <div class="dialogue-text">{d['jp_ruby']}</div>
        </div>
        ''')
    else:
        speaker_short = d['speaker'].split()[0]
        tab1_html.append(f'''
        <div class="dialogue-item" id="row-d-{d['id']}" onclick="toggleRowPlay({d['id']})">
          <div class="row-audio-ctrls" onclick="event.stopPropagation();">
            <button class="row-play-btn" id="row-play-btn-{d['id']}" title="재생 / 일시정지" onclick="toggleRowPlay({d['id']})">▶</button>
            <button class="row-stop-btn" id="row-stop-btn-{d['id']}" title="정지" onclick="stopSentence({d['id']})">⏹</button>
          </div>
          <div class="speaker-name {d['speaker_class']}">{speaker_short}</div>
          <div class="dialogue-text">{d['jp_ruby']}</div>
        </div>
        ''')

tab1_content = "\n".join(tab1_html)

# Generate Tab 2 (문장별 분석) HTML
tab2_html = []
current_scene = None

for d in dialogues:
    if d['scene'] != current_scene:
        current_scene = d['scene']
        scene_title = "구로몬 시장 구경과 해산물 구이" if current_scene == 1 else "과일가게에서의 흥정"
        tab2_html.append(f'''
        <div class="scene-header">
          📍 장면 {current_scene}: {scene_title}
        </div>
        ''')

    speaker_display = f"👤 {d['speaker']}" if d['is_stage'] else f"🗣️ {d['speaker']}"
    
    # Vocabulary list
    vocab_items = "".join([f"<li><strong>{v[0]}</strong>: {v[1]}</li>" for v in d.get('vocab', [])])
    if not vocab_items:
        vocab_items = "<li>해당 문장의 기본 어휘를 복습하세요.</li>"

    # Grammar list
    grammar_items = "".join([f"<li><strong>{g[0]}</strong>: {g[1]}</li>" for g in d.get('grammar', [])])
    if not grammar_items:
        grammar_items = "<li>회화 표현을 익혀보세요.</li>"

    # Kanji list
    kanji_items = []
    for k_pair in d.get('kanji', []):
        pair_str = " &nbsp;&nbsp; ".join([k for k in k_pair if k])
        if pair_str:
            kanji_items.append(f"<li>{pair_str}</li>")
    kanji_html = "".join(kanji_items) if kanji_items else "<li>(해당 없음)</li>"

    tab2_html.append(f'''
      <div class="card-item {d['speaker_class']}-card" id="card-d-{d['id']}">
        <div class="card-header-row">
          <div class="card-speaker {d['speaker_class']}">
            {speaker_display}
          </div>
          <div class="card-audio-ctrls" onclick="event.stopPropagation();">
            <button class="card-btn card-btn-play1" id="card-btn-play1-{d['id']}" onclick="toggleCardPlay1({d['id']})">▶ 1회 듣기</button>
            <button class="card-btn card-btn-play3" id="card-btn-play3-{d['id']}" onclick="toggleCardPlay3({d['id']})">🔁 3회 반복</button>
            <button class="card-btn card-btn-stop" id="card-btn-stop-{d['id']}" onclick="stopSentence({d['id']})">⏹ 정지</button>
          </div>
        </div>

        <div class="card-japanese" onclick="toggleCardPlay1({d['id']})" title="터치하여 재생">
          {d['jp_ruby']}
        </div>

        <div class="card-pron">{d['pron']}</div>
        <div class="card-ko">{d['ko']}</div>

        <div class="card-details-grid">
          <div class="details-box">
            <h4>📘 단어 정리</h4>
            <ul>{vocab_items}</ul>
          </div>
          <div class="details-box">
            <h4>💡 문법 & 관용어</h4>
            <ul>{grammar_items}</ul>
          </div>
          <div class="details-box">
            <h4>✍️ 한자 음과 뜻</h4>
            <ul>{kanji_html}</ul>
          </div>
        </div>
      </div>
    ''')

tab2_content = "\n".join(tab2_html)

dialogues_js = json.dumps(dialogues, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>제2과 구로몬 시장(黒門市場) 회화문 - 인터랙티브 학습 노트</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --ruby-color: #1d4ed8;
      --text-main: #0f172a;
      --text-sub: #475569;
      --border-line: #cbd5e1;
      --mire-color: #0284c7;
      --manami-color: #059669;
      --ojisan-color: #d97706;
      --stage-color: #64748b;
      --font-scale: 1.0;
    }}

    body.font-large {{ --font-scale: 1.25; }}
    body.font-xlarge {{ --font-scale: 1.5; }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      width: 100%;
      min-height: 100%;
      background-color: #ffffff !important;
      color: var(--text-main);
      font-family: 'Noto Sans KR', 'Noto Sans JP', sans-serif;
      line-height: 1.6;
      -webkit-text-size-adjust: 100%;
      overflow-x: hidden;
    }}

    /* 모바일 줌인 시 텍스트 탈출 방지 */
    .dialogue-text, .card-japanese, .card-pron, .card-ko, .details-box li {{
      overflow-wrap: anywhere !important;
      word-break: break-all !important;
    }}

    .container {{
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
      padding: 10px 14px 40px;
      background-color: #ffffff !important;
    }}

    /* 상단 헤더: PDF처럼 상하 분리 없는 일체형 배치 */
    .header-area {{
      position: static !important;
      background: #ffffff !important;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 12px;
      margin-bottom: 12px;
    }}

    /* 1단: 타이틀 + 우측 다운로드 버튼 나란히 배치 */
    .top-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}

    .title-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .title-group h1 {{
      font-size: calc(1.15rem * var(--font-scale));
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.5px;
    }}

    .badge-sub {{
      font-size: 0.76rem;
      background: #eff6ff;
      color: var(--primary);
      padding: 2px 7px;
      border-radius: 9999px;
      font-weight: 600;
      border: 1px solid #bfdbfe;
    }}

    .download-btns-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .btn-save-top {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 5px 10px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      text-decoration: none;
      transition: all 0.2s;
    }}

    .btn-save-html {{
      background: #f0fdf4;
      color: #16a34a;
      border-color: #bbf7d0;
    }}
    .btn-save-html:hover {{
      background: #dcfce7;
    }}

    .btn-save-pdf {{
      background: #fef2f2;
      color: #dc2626;
      border-color: #fecaca;
    }}
    .btn-save-pdf:hover {{
      background: #fee2e2;
    }}

    /* 2단: 탭 전환 바 */
    .tabs-row {{
      display: flex;
      gap: 6px;
      margin-bottom: 8px;
    }}

    .tab-btn {{
      flex: 1;
      padding: 9px 0;
      font-size: calc(0.95rem * var(--font-scale));
      font-weight: 700;
      border-radius: 6px;
      cursor: pointer;
      border: 1px solid var(--primary);
      background: #ffffff;
      color: #475569;
      transition: all 0.2s;
    }}

    .tab-btn.active {{
      background: var(--primary) !important;
      color: #ffffff !important;
    }}

    /* 3단: 글자크기 및 후리가나 토글 */
    .sub-tools-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 8px;
      font-size: 0.84rem;
      color: var(--text-sub);
    }}

    .font-size-group, .study-toggle-group {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .tool-btn {{
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #334155;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.8rem;
      cursor: pointer;
      font-weight: 500;
    }}

    .tool-btn.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      font-weight: 700;
    }}

    .btn-ruby-toggle {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      font-weight: 700;
    }}
    .btn-ruby-toggle.ruby-off {{
      background: #ffffff !important;
      color: #64748b !important;
      border-color: #cbd5e1 !important;
      font-weight: 500 !important;
    }}

    /* 4단: 상단 메인 오디오 플레이어 바 */
    .player-bar {{
      background: #0f172a;
      border-radius: 8px;
      padding: 8px 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(0,0,0,0.12);
    }}

    .player-left {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    .btn-play-all {{
      background: #38bdf8;
      color: #0f172a;
      border: none;
      border-radius: 5px;
      padding: 6px 12px;
      font-size: 0.86rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: background 0.2s;
    }}

    .btn-play-all.playing {{
      background: #f59e0b;
      color: #ffffff;
    }}

    .btn-stop-audio {{
      background: #334155;
      color: #ffffff;
      border: 1px solid #475569;
      border-radius: 5px;
      padding: 6px 10px;
      font-size: 0.86rem;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-stop-audio.is-stopped {{
      background: #ef4444 !important;
      border-color: #dc2626 !important;
      color: #ffffff !important;
    }}

    /* 선두 시작 티커 마퀴 애니메이션 (한글/화자명 없이 순수 일본어만) */
    .player-ticker-wrap {{
      flex: 1;
      overflow: hidden;
      white-space: nowrap;
      position: relative;
      height: 24px;
      display: flex;
      align-items: center;
    }}

    .ticker-content {{
      display: inline-block;
      font-size: 0.88rem;
      color: #ffffff !important;
      font-weight: 500;
    }}

    .marquee-scroll {{
      padding-left: 0;
      display: inline-block;
      white-space: nowrap;
      animation: ticker-start-front 11s linear infinite;
    }}

    @keyframes ticker-start-front {{
      0% {{ transform: translateX(0); }}
      16% {{ transform: translateX(0); }}
      100% {{ transform: translateX(-100%); }}
    }}

    .player-right select {{
      background: #1e293b;
      color: #ffffff;
      border: 1px solid #475569;
      border-radius: 4px;
      font-size: 0.78rem;
      padding: 3px 5px;
      cursor: pointer;
    }}

    /* 본문 영역 */
    .view-content {{
      display: none;
      width: 100%;
    }}
    .view-content.active {{
      display: block;
    }}

    .scene-header {{
      background: #f0fdf4;
      color: #166534;
      border-left: 4px solid #22c55e;
      padding: 7px 10px;
      margin: 16px 0 10px;
      font-weight: 700;
      font-size: calc(0.96rem * var(--font-scale));
      border-radius: 4px;
    }}

    /* 탭 1: 원문 대화 리스트 */
    .dialogue-item {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
      padding: 9px 6px;
      border-radius: 8px;
      transition: background-color 0.2s;
      cursor: pointer;
      border-bottom: 1px solid #f1f5f9;
    }}
    .dialogue-item:hover {{
      background-color: #f8fafc;
    }}
    .dialogue-item.playing {{
      background-color: #fefce8 !important;
      border-left: 3px solid #eab308;
    }}
    .dialogue-item.stage-item {{
      background-color: #fafaf9;
      color: #475569;
      font-style: normal;
    }}

    /* 원문보기 행 플레이어 컨트롤 */
    .row-audio-ctrls {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-shrink: 0;
      margin-top: 3px;
    }}

    .row-play-btn {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      background: var(--primary);
      color: #ffffff;
      font-size: 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
      box-shadow: 0 1px 2px rgba(37,99,235,0.2);
    }}
    .row-play-btn.playing {{
      background: #f59e0b;
    }}
    .row-play-btn.paused {{
      background: #2563eb;
    }}

    .row-stop-btn {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #64748b;
      font-size: 10px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }}
    .row-stop-btn:active {{
      background: #fee2e2;
      color: #ef4444;
      border-color: #fca5a5;
    }}

    .speaker-name {{
      width: 48px;
      font-weight: 700;
      font-size: calc(0.96rem * var(--font-scale));
      flex-shrink: 0;
      margin-top: 3px;
    }}
    .speaker-mire {{ color: var(--mire-color); }}
    .speaker-manami {{ color: var(--manami-color); }}
    .speaker-ojisan {{ color: var(--ojisan-color); }}
    .speaker-stage {{ color: var(--stage-color); }}

    .dialogue-text {{
      flex: 1;
      font-family: 'Noto Sans JP', sans-serif;
      font-size: calc(1.15rem * var(--font-scale));
      line-height: 2.2;
      color: #1e293b;
    }}

    /* 탭 2: 문장별 상세 분석 카드 */
    .card-item {{
      width: 100%;
      border: 1px solid var(--border-line);
      border-radius: 8px;
      padding: 14px 12px;
      margin-bottom: 16px;
      background: #ffffff;
      border-left: 5px solid #cbd5e1;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}

    .card-item.speaker-mire-card {{ border-left-color: var(--mire-color); }}
    .card-item.speaker-manami-card {{ border-left-color: var(--manami-color); }}
    .card-item.speaker-ojisan-card {{ border-left-color: var(--ojisan-color); }}
    .card-item.speaker-stage-card {{ border-left-color: var(--stage-color); background: #fafaf9; }}

    .card-item.playing {{
      background: #fefce8 !important;
      border-color: #facc15;
      border-left-color: #eab308;
    }}

    .card-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
      border-bottom: 1px dashed #e2e8f0;
      padding-bottom: 8px;
    }}

    .card-speaker {{
      font-weight: 700;
      font-size: calc(1.02rem * var(--font-scale));
    }}

    .card-audio-ctrls {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .card-btn {{
      border: none;
      border-radius: 6px;
      padding: 5px 9px;
      font-size: calc(0.82rem * var(--font-scale));
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }}

    .card-btn-play1 {{
      background: #eff6ff;
      color: var(--primary);
      border: 1px solid #bfdbfe;
    }}
    .card-btn-play1.playing {{
      background: #f59e0b;
      color: #ffffff;
      border-color: #f59e0b;
    }}

    .card-btn-play3 {{
      background: #f0fdf4;
      color: #16a34a;
      border: 1px solid #bbf7d0;
    }}
    .card-btn-play3.playing {{
      background: #16a34a;
      color: #ffffff;
      border-color: #16a34a;
    }}

    .card-btn-stop {{
      background: #f8fafc;
      color: #64748b;
      border: 1px solid #cbd5e1;
    }}
    .card-btn-stop:active {{
      background: #fee2e2;
      color: #ef4444;
      border-color: #fca5a5;
    }}

    .card-japanese {{
      font-family: 'Noto Sans JP', sans-serif;
      font-size: calc(1.26rem * var(--font-scale));
      line-height: 2.3;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 8px;
      cursor: pointer;
      width: 100%;
    }}

    .card-pron {{
      font-size: calc(0.94rem * var(--font-scale));
      color: #d97706;
      margin-bottom: 6px;
      line-height: 1.5;
      width: 100%;
    }}

    .card-ko {{
      font-size: calc(1.02rem * var(--font-scale));
      color: #334155;
      font-weight: 500;
      margin-bottom: 12px;
      line-height: 1.5;
      width: 100%;
    }}

    /* 상세 설명 박스 */
    .card-details-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin-top: 14px;
    }}

    .details-box {{
      background: #f8fafc;
      border-radius: 6px;
      padding: 10px 12px;
      border: 1px solid #e2e8f0;
    }}

    .details-box h4 {{
      font-size: calc(0.92rem * var(--font-scale));
      color: #1e293b;
      margin-bottom: 7px;
      display: flex;
      align-items: center;
      gap: 4px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
    }}

    .details-box ul {{
      list-style: none;
      padding-left: 0;
    }}

    .details-box li {{
      font-size: calc(0.88rem * var(--font-scale));
      line-height: 1.65;
      margin-bottom: 6px;
      color: #334155;
      border-bottom: 1px dotted #e2e8f0;
      padding-bottom: 4px;
    }}
    .details-box li:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .details-box strong {{
      color: #0f172a;
    }}

    /* 후리가나 숨기기 토글 */
    ruby {{
      ruby-align: center;
    }}
    rt {{
      font-size: 0.65em;
      color: var(--ruby-color);
      font-weight: 700;
      user-select: none;
    }}
    body.hide-ruby rt {{
      display: none !important;
    }}

    /* 반응형 */
    @media (min-width: 640px) {{
      .card-details-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .card-details-grid .details-box:last-child {{
        grid-column: span 2;
      }}
    }}
  </style>
</head>
<body>

  <!-- 카카오톡 인앱 브라우저 탈출 스크립트 -->
  <script>
    (function() {{
      const ua = navigator.userAgent.toLowerCase();
      if (ua.indexOf('kakaotalk') > -1 && ua.indexOf('android') > -1) {{
        location.href = 'intent://' + location.host + location.pathname + '#Intent;scheme=https;package=com.android.chrome;end';
      }}
    }})();
  </script>

  <div class="container">
    
    <!-- 상단 헤더 -->
    <header class="header-area">
      
      <!-- 1단: 타이틀 + 우측 다운로드 버튼 -->
      <div class="top-header-row">
        <div class="title-group">
          <h1>第2課 黒門市場 (제2과 구로몬 시장)</h1>
          <span class="badge-sub">제2과 회화</span>
        </div>
        <div class="download-btns-group">
          <button class="btn-save-top btn-save-html" onclick="downloadHtmlFile()" title="음성이 내장된 독립 웹문서로 저장">
            📥 HTML 저장
          </button>
          <a class="btn-save-top btn-save-pdf" href="./lesson2_note.pdf" target="_blank" download="제2과_구로몬시장_회화문_학습노트.pdf" title="원문 교재 PDF 열람 및 인쇄">
            📄 PDF 저장
          </a>
        </div>
      </div>

      <!-- 2단: 탭 전환 바 -->
      <div class="tabs-row">
        <button class="tab-btn active" id="tabBtn1" onclick="switchTab('tab1')">📖 원문 보기</button>
        <button class="tab-btn" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 분석</button>
      </div>

      <!-- 3단: 글자크기 및 후리가나 토글 -->
      <div class="sub-tools-row">
        <div class="font-size-group">
          <span>글자:</span>
          <button class="tool-btn active" id="fontNormalBtn" onclick="setFontScale('normal')">보통</button>
          <button class="tool-btn" id="fontLargeBtn" onclick="setFontScale('large')">크게</button>
          <button class="tool-btn" id="fontXLargeBtn" onclick="setFontScale('xlarge')">아주크게</button>
        </div>
        <div class="study-toggle-group">
          <button class="tool-btn btn-ruby-toggle" id="btnToggleRuby" onclick="toggleRuby()">후리가나</button>
          <button class="tool-btn" onclick="window.print()">🖨️ 인쇄</button>
        </div>
      </div>

      <!-- 4단: 상단 메인 오디오 플레이어 바 -->
      <div class="player-bar">
        <div class="player-left">
          <button class="btn-play-all" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체듣기</button>
          <button class="btn-stop-audio" id="btnStop" onclick="userStopAudio()" title="정지">⏹ 정지</button>
        </div>

        <div class="player-ticker-wrap">
          <div class="ticker-content" id="nowPlayingText">문장을 터치하거나 재생 버튼을 누르면 음성이 재생됩니다.</div>
        </div>

        <div class="player-right">
          <select id="speedSelect" onchange="setSpeed(this.value)">
            <option value="0.8">0.8x</option>
            <option value="1.0" selected>1.0x</option>
            <option value="1.2">1.2x</option>
          </select>
        </div>
      </div>

    </header>

    <!-- 오디오 엘리먼트 (Base64 인라인 내장: data:audio/mp3;base64,... 필수) -->
    <audio id="mainAudio" preload="auto">
      <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
    </audio>

    <!-- 탭 1: 원문 보기 -->
    <main id="tab1" class="view-content active">
      {tab1_content}
    </main>

    <!-- 탭 2: 문장별 상세 분석 -->
    <main id="tab2" class="view-content">
      {tab2_content}
    </main>

  </div>

  <script>
    const dialogues = {dialogues_js};

    const audio = document.getElementById('mainAudio');
    const nowPlayingText = document.getElementById('nowPlayingText');
    const btnPlayAll = document.getElementById('btnPlayAll');
    const btnStop = document.getElementById('btnStop');

    // 재생 상태 변수
    let currentMode = null; // null, 'all', 'single', 'repeat3'
    let currentSentenceId = null;
    let sentenceTimeout = null;
    let repeatRemaining = 0;

    // 글자 크기 변경
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

    // [요청 1 반영] 탭 전환 시 진행 중인 음성 즉시 정지
    function switchTab(tabId) {{
      stopAudio();
      setTickerText('문장을 터치하거나 재생 버튼을 누르면 음성이 재생됩니다.', false);

      document.querySelectorAll('.view-content').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      
      const tab1 = document.getElementById('tabBtn1');
      const tab2 = document.getElementById('tabBtn2');

      if (tabId === 'tab1') {{
        tab1.classList.add('active');
        tab2.classList.remove('active');
      }} else {{
        tab2.classList.add('active');
        tab1.classList.remove('active');
      }}
    }}

    // 후리가나 토글
    function toggleRuby() {{
      document.body.classList.toggle('hide-ruby');
      const isHidden = document.body.classList.contains('hide-ruby');
      const btn = document.getElementById('btnToggleRuby');
      if (isHidden) {{
        btn.classList.add('ruby-off');
      }} else {{
        btn.classList.remove('ruby-off');
      }}
    }}

    // [요청 2 반영] 지문 티커: 한글빼고 사람이름빼고 오직 일본어 원문만 출력
    function setTickerText(text, isScroll) {{
      nowPlayingText.className = 'ticker-content' + (isScroll ? ' marquee-scroll' : '');
      nowPlayingText.innerText = text;
    }}

    // 모든 UI 버튼 상태 동기화
    function updatePlaybackUI() {{
      // 상단 전체듣기 버튼
      if (currentMode === 'all') {{
        if (!audio.paused) {{
          btnPlayAll.classList.add('playing');
          btnPlayAll.innerText = '⏸ 일시정지';
        }} else {{
          btnPlayAll.classList.remove('playing');
          btnPlayAll.innerText = '▶ 전체듣기';
        }}
      }} else {{
        btnPlayAll.classList.remove('playing');
        btnPlayAll.innerText = '▶ 전체듣기';
      }}

      // 각 행 및 카드 버튼 상태 업데이트
      dialogues.forEach(d => {{
        const id = d.id;
        const rowPlayBtn = document.getElementById('row-play-btn-' + id);
        const cardPlay1Btn = document.getElementById('card-btn-play1-' + id);
        const cardPlay3Btn = document.getElementById('card-btn-play3-' + id);

        const isThis = (currentSentenceId === id);
        const isPlayingThis = isThis && !audio.paused;

        // 원문보기 행 버튼
        if (rowPlayBtn) {{
          if (isPlayingThis) {{
            rowPlayBtn.innerText = '⏸';
            rowPlayBtn.classList.add('playing');
            rowPlayBtn.classList.remove('paused');
          }} else if (isThis && audio.paused && currentMode !== null) {{
            rowPlayBtn.innerText = '▶';
            rowPlayBtn.classList.remove('playing');
            rowPlayBtn.classList.add('paused');
          }} else {{
            rowPlayBtn.innerText = '▶';
            rowPlayBtn.classList.remove('playing', 'paused');
          }}
        }}

        // 문장별 분석 1회 듣기
        if (cardPlay1Btn) {{
          if (currentMode === 'single' && isThis) {{
            if (isPlayingThis) {{
              cardPlay1Btn.innerText = '⏸ 일시정지';
              cardPlay1Btn.classList.add('playing');
            }} else {{
              cardPlay1Btn.innerText = '▶ 이어듣기';
              cardPlay1Btn.classList.remove('playing');
            }}
          }} else {{
            cardPlay1Btn.innerText = '▶ 1회 듣기';
            cardPlay1Btn.classList.remove('playing');
          }}
        }}

        // 문장별 분석 3회 반복
        if (cardPlay3Btn) {{
          if (currentMode === 'repeat3' && isThis) {{
            const round = 4 - repeatRemaining;
            if (isPlayingThis) {{
              cardPlay3Btn.innerText = `⏸ 반복중 (${{round}}/3)`;
              cardPlay3Btn.classList.add('playing');
            }} else {{
              cardPlay3Btn.innerText = `▶ 이어듣기 (${{round}}/3)`;
              cardPlay3Btn.classList.remove('playing');
            }}
          }} else {{
            cardPlay3Btn.innerText = '🔁 3회 반복';
            cardPlay3Btn.classList.remove('playing');
          }}
        }}
      }});
    }}

    // [전체듣기 토글]
    function togglePlayAll() {{
      if (currentMode === 'all') {{
        if (!audio.paused) {{
          audio.pause();
          setTickerText('⏸ 전체 재생이 일시 정지되었습니다.', false);
        }} else {{
          audio.play().catch(e => console.error(e));
          const d = dialogues.find(x => audio.currentTime >= x.start && audio.currentTime < x.end);
          if (d) setTickerText(d.jp_plain, true);
        }}
      }} else {{
        stopAudio();
        currentMode = 'all';
        audio.currentTime = 0;
        audio.play().catch(e => console.error(e));
        const d = dialogues[0];
        currentSentenceId = d.id;
        highlightSentence(d.id);
        setTickerText(d.jp_plain, true);
      }}
      updatePlaybackUI();
    }}

    audio.addEventListener('timeupdate', () => {{
      if (currentMode === 'all') {{
        const cur = audio.currentTime;
        const currentD = dialogues.find(d => cur >= d.start && cur < d.end);
        if (currentD && currentD.id !== currentSentenceId) {{
          currentSentenceId = currentD.id;
          highlightSentence(currentD.id);
          // [요청 2 반영] 순수 일본어 문장만 노출
          setTickerText(currentD.jp_plain, true);
          updatePlaybackUI();
        }}
      }}
    }});

    audio.addEventListener('ended', () => {{
      stopAudio();
      setTickerText('🎉 전체 회화 재생이 완료되었습니다!', false);
    }});

    // [개별 문장 재생 실행 함수]
    function playSentenceSlice(id, start, end) {{
      currentSentenceId = id;
      highlightSentence(id);

      const d = dialogues.find(x => x.id === id);
      // [요청 2 반영] 오직 일본어 원문만 흘러감
      setTickerText(d.jp_plain, true);

      audio.currentTime = start;
      const playPromise = audio.play();
      if (playPromise !== undefined) {{
        playPromise.catch(e => console.error("Playback error:", e));
      }}
      updatePlaybackUI();

      const duration = (end - start) * 1000 / audio.playbackRate;
      if (sentenceTimeout) clearTimeout(sentenceTimeout);

      sentenceTimeout = setTimeout(() => {{
        onSentenceComplete(id, start, end);
      }}, duration);
    }}

    function onSentenceComplete(id, start, end) {{
      if (currentMode === 'repeat3') {{
        repeatRemaining--;
        if (repeatRemaining > 0) {{
          audio.pause();
          sentenceTimeout = setTimeout(() => {{
            if (currentMode === 'repeat3' && currentSentenceId === id) {{
              playSentenceSlice(id, start, end);
            }}
          }}, 450);
          updatePlaybackUI();
          return;
        }} else {{
          stopAudio();
          setTickerText('✅ 3회 반복 듣기가 완료되었습니다.', false);
        }}
      }} else if (currentMode === 'single') {{
        stopAudio();
        setTickerText('✅ 1회 듣기가 완료되었습니다.', false);
      }}
      updatePlaybackUI();
    }}

    // [요청 3 반영] 원문보기 행 플레이어 토글 (재생 / 일시정지)
    function toggleRowPlay(id) {{
      const d = dialogues.find(x => x.id === id);
      if (!d) return;

      if (currentSentenceId === id && currentMode === 'single') {{
        if (!audio.paused) {{
          if (sentenceTimeout) clearTimeout(sentenceTimeout);
          audio.pause();
          setTickerText('⏸ 일시 정지되었습니다.', false);
        }} else {{
          audio.play().catch(e => console.error(e));
          setTickerText(d.jp_plain, true);
          const remaining = Math.max(0.1, (d.end - audio.currentTime)) * 1000 / audio.playbackRate;
          sentenceTimeout = setTimeout(() => {{
            onSentenceComplete(id, d.start, d.end);
          }}, remaining);
        }}
        updatePlaybackUI();
      }} else {{
        stopAudio();
        currentMode = 'single';
        repeatRemaining = 1;
        playSentenceSlice(id, d.start, d.end);
      }}
    }}

    // [요청 4 반영] 문장별 분석 1회 듣기 토글
    function toggleCardPlay1(id) {{
      const d = dialogues.find(x => x.id === id);
      if (!d) return;

      if (currentSentenceId === id && currentMode === 'single') {{
        if (!audio.paused) {{
          if (sentenceTimeout) clearTimeout(sentenceTimeout);
          audio.pause();
          setTickerText('⏸ 일시 정지되었습니다.', false);
        }} else {{
          audio.play().catch(e => console.error(e));
          setTickerText(d.jp_plain, true);
          const remaining = Math.max(0.1, (d.end - audio.currentTime)) * 1000 / audio.playbackRate;
          sentenceTimeout = setTimeout(() => {{
            onSentenceComplete(id, d.start, d.end);
          }}, remaining);
        }}
        updatePlaybackUI();
      }} else {{
        stopAudio();
        currentMode = 'single';
        repeatRemaining = 1;
        playSentenceSlice(id, d.start, d.end);
      }}
    }}

    // [요청 4 반영] 문장별 분석 3회 반복 토글
    function toggleCardPlay3(id) {{
      const d = dialogues.find(x => x.id === id);
      if (!d) return;

      if (currentSentenceId === id && currentMode === 'repeat3') {{
        if (!audio.paused) {{
          if (sentenceTimeout) clearTimeout(sentenceTimeout);
          audio.pause();
          setTickerText('⏸ 3회 반복이 일시 정지되었습니다.', false);
        }} else {{
          audio.play().catch(e => console.error(e));
          setTickerText(d.jp_plain, true);
          const remaining = Math.max(0.1, (d.end - audio.currentTime)) * 1000 / audio.playbackRate;
          sentenceTimeout = setTimeout(() => {{
            onSentenceComplete(id, d.start, d.end);
          }}, remaining);
        }}
        updatePlaybackUI();
      }} else {{
        stopAudio();
        currentMode = 'repeat3';
        repeatRemaining = 3;
        playSentenceSlice(id, d.start, d.end);
      }}
    }}

    // 개별 정지 버튼 (원문보기 및 문장별 분석 카드 정지)
    function stopSentence(id) {{
      stopAudio();
      btnStop.classList.add('is-stopped');
      setTickerText('⏹ 오디오가 정지되었습니다.', false);
      setTimeout(() => {{
        btnStop.classList.remove('is-stopped');
      }}, 1000);
    }}

    // 상단 플레이어 정지 버튼
    function userStopAudio() {{
      stopSentence(currentSentenceId);
    }}

    function stopAudio() {{
      if (sentenceTimeout) {{
        clearTimeout(sentenceTimeout);
        sentenceTimeout = null;
      }}
      audio.pause();
      currentMode = null;
      currentSentenceId = null;
      repeatRemaining = 0;
      stopHighlight();
      updatePlaybackUI();
    }}

    function highlightSentence(id) {{
      stopHighlight();
      const row = document.getElementById('row-d-' + id);
      const card = document.getElementById('card-d-' + id);
      if (row) row.classList.add('playing');
      if (card) card.classList.add('playing');
    }}

    function stopHighlight() {{
      document.querySelectorAll('.dialogue-item').forEach(el => el.classList.remove('playing'));
      document.querySelectorAll('.card-item').forEach(el => el.classList.remove('playing'));
    }}

    function setSpeed(rate) {{
      audio.playbackRate = parseFloat(rate);
    }}

    function downloadHtmlFile() {{
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
  </script>
</body>
</html>
'''

target_paths = [
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/2/index.html',
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/index.html',
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/lesson2.html',
    '/Users/kwangyulllee/Desktop/일본어/일본어활용1/제2과_구로몬시장_인터랙티브_학습노트.html',
    '/Users/kwangyulllee/Desktop/일본어/제2과_구로몬시장_인터랙티브_학습노트.html'
]

for p in target_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Updated {p} ({len(html_content):,} bytes)")

print("Generation completed successfully!")
