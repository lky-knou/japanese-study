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

    /* 텍스트 자동 줄바꿈 */
    .dialogue-text, 
    .card-japanese, 
    .card-pron, 
    .card-ko, 
    .details-box ul li {{
      word-break: break-all !important;
      overflow-wrap: anywhere !important;
      word-wrap: break-word !important;
      white-space: normal !important;
    }}

    /* ============================================================
       상단 헤더
       ============================================================ */
    header.paper-header {{
      width: 100%;
      background: #ffffff;
      border-bottom: 2px solid #0f172a;
      padding: 10px 12px 10px 12px;
      max-width: 800px;
      margin: 0 auto;
    }}

    /* [요청 1 반영] 1행: 좌측 제목 ↔ 우측 끝 저장 버튼 2개 (1줄 완벽 정렬) */
    .top-brand-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
      width: 100%;
    }}

    .title-wrap {{
      display: flex;
      align-items: center;
      gap: 5px;
      flex-shrink: 1;
      min-width: 0;
    }}

    .title-wrap h1 {{
      font-size: calc(1.08rem * var(--font-scale));
      font-weight: 700;
      color: #0f172a;
      margin: 0;
      white-space: nowrap;
      letter-spacing: -0.4px;
    }}

    .title-wrap .badge {{
      background: #e0e7ff;
      color: #3730a3;
      font-size: 0.68rem;
      padding: 2px 6px;
      border-radius: 9999px;
      font-weight: 600;
      white-space: nowrap;
    }}

    .download-actions {{
      display: flex;
      align-items: center;
      gap: 5px;
      flex-shrink: 0;
    }}

    .btn-action {{
      font-family: inherit;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 5px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 3px;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap;
      border: 1px solid transparent;
    }}

    .btn-action:active {{
      transform: scale(0.97);
    }}

    .btn-html {{
      background: #ecfdf5;
      color: #047857;
      border-color: #a7f3d0;
    }}

    .btn-pdf {{
      background: #fef2f2;
      color: #b91c1c;
      border-color: #fecaca;
    }}

    /* 2행: 50:50 세그먼트 탭 바 */
    .nav-tab-bar {{
      display: flex;
      width: 100%;
      background: #f8fafc;
      border-radius: 8px;
      padding: 3px;
      gap: 5px;
      margin-bottom: 8px;
      border: 1px solid #cbd5e1;
    }}

    .tab-segment {{
      flex: 1;
      text-align: center;
      padding: 8px 0;
      font-size: 0.88rem;
      font-weight: 700;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      -webkit-tap-highlight-color: transparent;
      background: #ffffff;
      color: #475569;
      border: 1px solid #cbd5e1;
    }}

    .tab-segment.active {{
      background: var(--primary) !important;
      color: #ffffff !important;
      border-color: var(--primary) !important;
      box-shadow: 0 2px 4px rgba(37, 99, 235, 0.25);
    }}

    /* 3행: 학습 옵션 툴바 */
    .options-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #ffffff;
      padding: 2px 0 6px 0;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .opt-group {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: wrap;
    }}

    .opt-label {{
      font-size: 0.74rem;
      color: var(--text-sub);
      font-weight: 700;
      margin-right: 2px;
    }}

    .btn-chip {{
      font-family: inherit;
      font-size: 0.76rem;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
      -webkit-tap-highlight-color: transparent;
    }}

    .btn-chip.active {{
      background: var(--primary) !important;
      color: #ffffff !important;
      border-color: var(--primary) !important;
    }}

    #btnToggleRuby {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      font-weight: 700;
    }}

    #btnToggleRuby.ruby-off {{
      background: #ffffff !important;
      color: #475569 !important;
      border-color: #cbd5e1 !important;
      font-weight: 600;
    }}

    /* 4행: 일체형 플레이어 바 */
    .player-bar {{
      width: 100%;
      background: #0f172a;
      color: #ffffff;
      border-radius: 6px;
      padding: 7px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}

    .player-left {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }}

    /* [요청 2 반영] 전체연속듣기 -> 전체듣기로 변경 */
    .btn-play-all {{
      background: #38bdf8;
      color: #0f172a;
      border: none;
      padding: 6px 11px;
      border-radius: 5px;
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      white-space: nowrap;
    }}

    .btn-play-all.playing {{
      background: #facc15;
      color: #0f172a;
    }}

    .btn-stop {{
      background: #334155;
      color: #e2e8f0;
      border: 1px solid #475569;
      padding: 6px 9px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.15s;
      white-space: nowrap;
    }}

    .btn-stop.is-stopped {{
      background: #ef4444 !important;
      color: #ffffff !important;
      border-color: #ef4444 !important;
      box-shadow: 0 0 6px rgba(239, 68, 68, 0.5);
    }}

    /* ============================================================
       [요청 3 반영: 문장 앞에서 바로 시작하는 자막 흐름 애니메이션]
       ============================================================ */
    .ticker-viewport {{
      flex: 1;
      min-width: 0;
      overflow: hidden;
      position: relative;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 4px;
      padding: 5px 8px;
      margin: 0 4px;
      height: 32px;
      display: flex;
      align-items: center;
    }}

    .ticker-content {{
      white-space: nowrap;
      color: #ffffff !important; /* 순백색 */
      font-size: 0.84rem;
      font-weight: 600;
      display: inline-block;
      width: 100%;
    }}

    /*
      문장 시작 즉시 앞부분(첫 글자)이 왼쪽 앞에서 딱 뜬 상태로 시작!
      1.2초간 앞머리를 읽을 수 있게 정지 후 부드럽게 좌측 스크롤
    */
    .marquee-scroll {{
      display: inline-block;
      padding-left: 0 !important; /* 뒤에서 기어나오는 지연 완전 제거 */
      animation: marqueeFromStart 10s linear infinite;
    }}

    @keyframes marqueeFromStart {{
      0%   {{ transform: translateX(0); }}
      15%  {{ transform: translateX(0); }} /* 앞부분 1.5초 정지해 보여줌 */
      100% {{ transform: translateX(-100%); }}
    }}

    .speed-select {{
      background: #334155;
      color: white;
      border: 1px solid #475569;
      padding: 4px 6px;
      border-radius: 5px;
      font-size: 0.75rem;
      cursor: pointer;
      flex-shrink: 0;
    }}

    /* 본문 영역 */
    main.document-body {{
      width: 100%;
      max-width: 800px;
      margin: 12px auto;
      padding: 0 12px 60px 12px;
      background: #ffffff !important;
    }}

    ruby {{
      ruby-position: over;
      ruby-align: center;
      display: inline-ruby;
    }}

    rt {{
      font-size: 0.65em;
      color: var(--ruby-color);
      font-weight: 700;
      line-height: 1.0;
      user-select: none;
      transform: translateY(-2px);
    }}

    body.hide-ruby rt {{
      visibility: hidden;
      opacity: 0;
    }}

    .view-content {{
      display: none;
    }}
    .view-content.active {{
      display: block;
    }}

    /* 탭 1 */
    .dialogue-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
    }}

    .dialogue-item {{
      display: flex;
      gap: 10px;
      align-items: flex-start;
      padding: 8px 6px;
      border-radius: 6px;
      border-bottom: 1px solid #f1f5f9;
      cursor: pointer;
      width: 100%;
    }}

    .dialogue-item:active {{
      background: #f8fafc;
    }}

    .dialogue-item.playing {{
      background: #fef08a !important;
      border-radius: 6px;
      border-bottom-color: transparent;
    }}

    .play-btn-circle {{
      background: #e2e8f0;
      border: none;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.9rem;
      color: #1e293b;
      cursor: pointer;
      flex-shrink: 0;
      margin-top: 4px;
    }}

    .dialogue-item.playing .play-btn-circle {{
      background: #0f172a;
      color: #38bdf8;
    }}

    .speaker-name {{
      width: 58px;
      flex-shrink: 0;
      font-weight: 700;
      font-size: calc(1.02rem * var(--font-scale));
      padding-top: 6px;
    }}

    .speaker-mire {{ color: var(--mire-color); }}
    .speaker-manami {{ color: var(--manami-color); }}
    .speaker-ojisan {{ color: var(--ojisan-color); }}
    .speaker-stage {{ color: var(--stage-color); font-weight: normal; font-style: italic; }}

    .dialogue-text {{
      flex: 1;
      font-size: calc(1.22rem * var(--font-scale));
      line-height: 2.2;
      font-family: 'Noto Sans JP', sans-serif;
      color: #0f172a;
    }}

    .dialogue-item.stage-item {{
      background: #f8fafc;
      padding-left: 10px;
      border-left: 3px solid #94a3b8;
    }}

    .dialogue-item.stage-item .dialogue-text {{
      font-size: calc(1.02rem * var(--font-scale));
      color: #475569;
    }}

    /* 탭 2 */
    .scene-title {{
      background: #ecfdf5;
      border-left: 5px solid #059669;
      padding: 10px 12px;
      border-radius: 6px;
      margin: 18px 0 12px 0;
      font-weight: 700;
      color: #065f46;
      font-size: calc(1.1rem * var(--font-scale));
      width: 100%;
    }}

    .card-item {{
      width: 100%;
      border: 1px solid var(--border-line);
      border-radius: 8px;
      padding: 14px 12px;
      margin-bottom: 14px;
      background: #ffffff;
      border-left: 5px solid #cbd5e1;
      overflow: hidden;
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
      margin-bottom: 8px;
    }}

    .card-speaker {{
      font-weight: 700;
      font-size: calc(1.02rem * var(--font-scale));
    }}

    .card-japanese {{
      font-family: 'Noto Sans JP', sans-serif;
      font-size: calc(1.3rem * var(--font-scale));
      line-height: 2.3;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 8px;
      cursor: pointer;
      width: 100%;
    }}

    .card-pron {{
      font-size: calc(0.96rem * var(--font-scale));
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
      padding-bottom: 8px;
      border-bottom: 1px dashed var(--border-line);
      line-height: 1.55;
      width: 100%;
    }}

    .card-details-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 10px;
      background: #f8fafc;
      padding: 10px;
      border-radius: 6px;
      border: 1px solid var(--border-line);
      width: 100%;
    }}

    .details-box h4 {{
      font-size: 0.82rem;
      color: #475569;
      margin-bottom: 4px;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 3px;
    }}

    .details-box ul {{
      list-style: none;
      font-size: calc(0.88rem * var(--font-scale));
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .details-box ul li {{
      line-height: 1.45;
    }}

    .details-box ul li strong {{
      color: #0f172a;
    }}

    @media (max-width: 650px) {{
      .card-details-grid {{
        grid-template-columns: 1fr;
      }}
      .speaker-name {{
        width: 50px;
      }}
      main.document-body {{
        padding: 0 8px 60px 8px;
      }}
    }}

    @media print {{
      header.paper-header, .play-btn-circle, .btn-action, .options-bar, .player-bar {{
        display: none !important;
      }}
      body {{
        background: white;
        color: black;
      }}
      .view-content {{
        display: block !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- ============================================================
       상단 헤더
       ============================================================ -->
  <header class="paper-header">
    <!-- 1행: 좌측 타이틀 ↔ 우측 끝 저장 버튼 2개 -->
    <div class="top-brand-row">
      <div class="title-wrap">
        <h1>第2課 黒門市場</h1>
        <span class="badge">제2과 회화</span>
      </div>
      <div class="download-actions">
        <!-- 음성 포함 완전 독립형 HTML 저장 -->
        <button class="btn-action btn-html" onclick="downloadHtmlFile()" title="음성이 내장된 인터랙티브 HTML 파일 다운로드">
          📥 HTML 저장
        </button>
        <!-- 음성 없는 원본 교재 PDF 다운로드 -->
        <a class="btn-action btn-pdf" href="lesson2_note.pdf" download="제2과_구로몬시장_회화문_학습노트.pdf" title="음성 없는 교재 원본 PDF 다운로드">
          📄 PDF 저장
        </a>
      </div>
    </div>

    <!-- 2행: 가로 50:50 탭 전환 바 -->
    <div class="nav-tab-bar">
      <button class="tab-segment active" id="tabBtn1" onclick="switchTab('tab1')">📖 원문 보기</button>
      <button class="tab-segment" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 분석</button>
    </div>

    <!-- 3행: 학습 옵션 툴바 -->
    <div class="options-bar">
      <div class="opt-group">
        <span class="opt-label">글자:</span>
        <button class="btn-chip active" id="fontNormalBtn" onclick="setFontScale('normal')">보통</button>
        <button class="btn-chip" id="fontLargeBtn" onclick="setFontScale('large')">크게</button>
        <button class="btn-chip" id="fontXLargeBtn" onclick="setFontScale('xlarge')">아주크게</button>
      </div>
      <div class="opt-group">
        <button class="btn-chip" id="btnToggleRuby" onclick="toggleRuby()">후리가나</button>
        <button class="btn-chip" onclick="window.print()" title="화면 인쇄 / PDF 출력">🖨️ 인쇄</button>
      </div>
    </div>

    <!-- 4행: 일체형 플레이어 바 -->
    <div class="player-bar">
      <div class="player-left">
        <!-- 전체연속듣기 -> 전체듣기 -->
        <button class="btn-play-all" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체듣기</button>
        <button class="btn-stop" id="btnStop" onclick="userStopAudio()">⏹ 정지</button>
      </div>
      
      <!-- 지문 표시 뷰포트 (앞에서부터 즉시 읽을 수 있는 자막 흐름) -->
      <div class="ticker-viewport">
        <div class="ticker-content" id="nowPlayingText">
          문장을 터치하면 해당 음성이 재생됩니다.
        </div>
      </div>

      <select class="speed-select" id="speedSelect" onchange="setSpeed(parseFloat(this.value))">
        <option value="0.8">0.8x</option>
        <option value="1.0" selected>1.0x</option>
        <option value="1.2">1.2x</option>
      </select>
    </div>
  </header>

  <!-- 본문 영역 -->
  <main class="document-body">

    <!-- TAB 1: 회화문 전체 원문 -->
    <div id="tab1" class="view-content active">
      <div class="dialogue-list">
'''

# Generate Tab 1
for d in dialogues:
    stage_cls = "stage-item" if d["is_stage"] else ""
    spk_tag = f'<div class="speaker-name {d["speaker_class"]}">{d["speaker"].split()[0]}</div>' if not d["is_stage"] else ''
    html_content += f'''
        <div class="dialogue-item {stage_cls}" id="row-d-{d['id']}" onclick="playSentence({d['id']}, {d['start']}, {d['end']})">
          <button class="play-btn-circle" title="재생" onclick="event.stopPropagation(); playSentence({d['id']}, {d['start']}, {d['end']})">▶</button>
          {spk_tag}
          <div class="dialogue-text">{d['jp_ruby']}</div>
        </div>
'''

html_content += '''
      </div>
    </div>

    <!-- TAB 2: 문장별 상세 분석 -->
    <div id="tab2" class="view-content">
'''

# Generate Tab 2
current_scene = None
for d in dialogues:
    if d["scene"] != current_scene:
        current_scene = d["scene"]
        html_content += f'''
      <div class="scene-title">
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
      <div class="card-item {spk_card_cls}" id="card-d-{d['id']}">
        <div class="card-header-row">
          <div class="card-speaker {d['speaker_class']}">
            👤 {d['speaker']}
          </div>
          <button class="btn-chip" style="color: var(--primary); font-weight: bold;" onclick="playSentence({d['id']}, {d['start']}, {d['end']})">▶ 1회 듣기</button>
        </div>

        <div class="card-japanese" onclick="playSentence({d['id']}, {d['start']}, {d['end']})" title="터치하여 듣기">
          {d['jp_ruby']}
        </div>

        <div class="card-pron">[발음] {d['pron']}</div>
        <div class="card-ko">{d['ko']}</div>

        <div class="card-details-grid">
          <div class="details-box">
            <h4>📘 단어 정리</h4>
            <ul>{vocab_html}</ul>
          </div>
          <div class="details-box">
            <h4>💡 문법 & 관용어</h4>
            <ul>{grammar_html}</ul>
          </div>
          <div class="details-box">
            <h4>✍️ 한자 음과 뜻</h4>
            <ul>{kanji_html}</ul>
          </div>
        </div>
      </div>
'''

html_content += f'''
    </div>

  </main>

  <!-- Base64 Audio Element -->
  <audio id="mainAudio" preload="auto">
    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
  </audio>

  <script>
    const dialogues = {json.dumps(dialogues, ensure_ascii=False)};
    const audio = document.getElementById('mainAudio');
    const nowPlayingText = document.getElementById('nowPlayingText');
    const btnPlayAll = document.getElementById('btnPlayAll');
    const btnStop = document.getElementById('btnStop');

    let isPlayingAll = false;
    let currentSentenceId = null;
    let sentenceTimeout = null;

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

    // 탭 전환
    function switchTab(tabId) {{
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

    // 정지 버튼 클릭 시 피드백
    function userStopAudio() {{
      stopAudio();
      btnStop.classList.add('is-stopped');
      setTickerText('⏹ 오디오가 정지되었습니다.', false);
      setTimeout(() => {{
        btnStop.classList.remove('is-stopped');
      }}, 1200);
    }}

    // 지문 표시 함수
    function setTickerText(html, isScroll) {{
      nowPlayingText.className = 'ticker-content' + (isScroll ? ' marquee-scroll' : '');
      nowPlayingText.innerHTML = html;
    }}

    // 개별 문장 재생
    function playSentence(id, start, end) {{
      stopAudio();
      btnStop.classList.remove('is-stopped');
      currentSentenceId = id;
      const d = dialogues.find(x => x.id === id);
      highlightSentence(id);
      
      // 문장 앞머리부터 바로 보이도록 전달
      const textToDisplay = `<strong>[${{d.speaker.split()[0]}}]</strong> ${{d.jp_plain}}  ──  ${{d.ko}}`;
      setTickerText(textToDisplay, true);

      audio.currentTime = start;
      const p = audio.play();
      if (p !== undefined) p.catch(() => {{}});

      const duration = (end - start) * 1000 / audio.playbackRate;
      sentenceTimeout = setTimeout(() => {{
        audio.pause();
        stopHighlight();
        setTickerText('✅ 1회 듣기 완료 (문장 터치 시 다시 재생)', false);
        btnStop.classList.add('is-stopped');
        setTimeout(() => btnStop.classList.remove('is-stopped'), 1000);
      }}, duration);
    }}

    // 전체 재생 토글
    function togglePlayAll() {{
      if (isPlayingAll) {{
        audio.pause();
        isPlayingAll = false;
        btnPlayAll.classList.remove('playing');
        btnPlayAll.innerText = '▶ 전체듣기';
        btnStop.classList.add('is-stopped');
        setTickerText('⏸ 전체 재생이 일시 정지되었습니다.', false);
      }} else {{
        stopAudio();
        isPlayingAll = true;
        btnPlayAll.classList.add('playing');
        btnPlayAll.innerText = '⏸ 일시정지';
        btnStop.classList.remove('is-stopped');
        setTickerText('▶ 전체 재생 시작...', false);
        audio.currentTime = 0;
        audio.play().catch(() => {{}});
      }}
    }}

    // 전체 재생 중 문장 흐름 업데이트
    audio.addEventListener('timeupdate', () => {{
      if (isPlayingAll) {{
        const cur = audio.currentTime;
        const currentD = dialogues.find(d => cur >= d.start && cur < d.end);
        if (currentD && currentD.id !== currentSentenceId) {{
          currentSentenceId = currentD.id;
          highlightSentence(currentD.id);
          const fullText = `<strong>[${{currentD.speaker.split()[0]}}]</strong> ${{currentD.jp_plain}}  ──  ${{currentD.ko}}`;
          setTickerText(fullText, true);
        }}
      }}
    }});

    audio.addEventListener('ended', () => {{
      stopAudio();
      setTickerText('🎉 전체 회화 재생이 완료되었습니다!', false);
      btnStop.classList.add('is-stopped');
    }});

    function stopAudio() {{
      if (sentenceTimeout) {{
        clearTimeout(sentenceTimeout);
        sentenceTimeout = null;
      }}
      audio.pause();
      isPlayingAll = false;
      btnPlayAll.classList.remove('playing');
      btnPlayAll.innerText = '▶ 전체듣기';
      stopHighlight();
      currentSentenceId = null;
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
      audio.playbackRate = rate;
      document.getElementById('speedSelect').value = rate;
    }}

    // 오프라인 HTML 파일 다운로드
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

# Update all paths
paths = [
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/index.html',
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/lesson2.html',
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/2/index.html',
    '/Users/kwangyulllee/Desktop/일본어/일본어활용1/제2과_구로몬시장_인터랙티브_학습노트.html',
    '/Users/kwangyulllee/Desktop/일본어/제2과_구로몬시장_인터랙티브_학습노트.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Updated with header buttons on far right, '전체듣기', and front-start marquee!")
