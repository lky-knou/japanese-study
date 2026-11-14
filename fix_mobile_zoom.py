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
      --text-main: #0f172a;
      --text-sub: #475569;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --highlight: #fef08a;
      --highlight-border: #facc15;
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

    body {{
      font-family: 'Noto Sans KR', 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 80px;
      -webkit-text-size-adjust: 100%;
    }}

    /* 
      핵심 해결책 1: 
      position: sticky 대신 position: relative 사용! 
      -> 화면을 2배, 3배 확대하거나 스크롤할 때 헤더가 화면에 고정되어 본문을 가리는 현상을 100% 제거
    */
    header.app-header {{
      position: relative;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      box-shadow: 0 1px 4px rgba(0,0,0,0.05);
      padding: 10px 14px;
    }}

    .header-inner {{
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .header-title-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .header-title-bar h1 {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .header-title-bar span.badge {{
      background: #e0e7ff;
      color: #3730a3;
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    /* 슬림하고 깔끔한 모바일 툴바 */
    .toolbar-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .btn-group {{
      display: flex;
      align-items: center;
      gap: 5px;
      flex-wrap: wrap;
    }}

    button.btn, a.btn {{
      font-family: inherit;
      font-size: 0.82rem;
      padding: 6px 11px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
      font-weight: 600;
      white-space: nowrap;
      text-decoration: none;
      -webkit-tap-highlight-color: transparent;
    }}

    button.btn:active, a.btn:active {{
      transform: scale(0.97);
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

    button.btn-success, a.btn-success {{
      background: #059669;
      color: white;
      border-color: #059669;
    }}

    button.btn-sm {{
      padding: 4px 8px;
      font-size: 0.76rem;
    }}

    /* 추가 옵션 접이식 패널 (글자크기/숨김/배속) */
    #extraSettingsPanel {{
      display: none;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 10px 12px;
      margin-top: 6px;
      gap: 10px;
      flex-direction: column;
    }}

    #extraSettingsPanel.open {{
      display: flex;
    }}

    .settings-subrow {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .settings-label {{
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-sub);
      min-width: 55px;
    }}

    /* Main Container */
    main.container {{
      max-width: 900px;
      margin: 14px auto;
      padding: 0 10px;
    }}

    /* Ruby Furigana Styling (시원시원한 가독성) */
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
      transform: translateY(-3px);
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
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
      padding: 16px 14px;
    }}

    .paper-header {{
      border-bottom: 2px solid #0f172a;
      padding-bottom: 8px;
      margin-bottom: 16px;
    }}

    .paper-header h2 {{
      font-size: calc(1.35rem * var(--font-scale));
      color: #0f172a;
    }}

    .paper-header .sub {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-top: 4px;
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
      padding: 10px 10px;
      border-radius: 8px;
      transition: all 0.15s ease;
      cursor: pointer;
      border: 1px solid transparent;
      -webkit-tap-highlight-color: rgba(37, 99, 235, 0.1);
    }}

    .dialogue-row:active {{
      background: #f1f5f9;
    }}

    .dialogue-row.playing {{
      background: #fef9c3;
      border-color: #facc15;
      box-shadow: 0 2px 8px rgba(234, 179, 8, 0.2);
    }}

    .play-trigger-btn {{
      background: #e2e8f0;
      border: none;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      color: #334155;
      cursor: pointer;
      flex-shrink: 0;
      margin-top: 4px;
      transition: all 0.15s;
    }}

    .dialogue-row.playing .play-trigger-btn {{
      background: #eab308;
      color: white;
    }}

    .speaker-tag {{
      width: 65px;
      flex-shrink: 0;
      font-weight: 700;
      font-size: calc(1.05rem * var(--font-scale));
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
      font-size: calc(1.25rem * var(--font-scale));
      line-height: 2.2;
      font-family: 'Noto Sans JP', sans-serif;
      color: #0f172a;
      word-break: keep-all;
      overflow-wrap: break-word;
    }}

    .dialogue-row.stage-direction {{
      background: #f8fafc;
      border-left: 3px solid #94a3b8;
      padding-left: 12px;
    }}

    .dialogue-row.stage-direction .jp-line {{
      font-size: calc(1.1rem * var(--font-scale));
      color: #475569;
    }}

    /* View: Detailed Analysis Cards (Tab 2) */
    .scene-divider {{
      background: #ecfdf5;
      border: 1px solid #a7f3d0;
      border-left: 5px solid #059669;
      padding: 10px 14px;
      border-radius: 8px;
      margin: 20px 0 14px 0;
      font-weight: 700;
      color: #065f46;
      font-size: calc(1.1rem * var(--font-scale));
    }}

    .analysis-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
      padding: 16px 16px;
      margin-bottom: 16px;
      transition: all 0.15s ease;
      border-left: 5px solid #cbd5e1;
    }}

    .analysis-card.speaker-mire-card {{ border-left-color: var(--mire-color); }}
    .analysis-card.speaker-manami-card {{ border-left-color: var(--manami-color); }}
    .analysis-card.speaker-ojisan-card {{ border-left-color: var(--ojisan-color); }}
    .analysis-card.speaker-stage-card {{ border-left-color: var(--stage-color); background: #fafaf9; }}

    .analysis-card.playing {{
      border-color: #facc15;
      border-left-color: #eab308;
      background: #fefce8;
      box-shadow: 0 4px 14px rgba(234, 179, 8, 0.2);
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }}

    .card-speaker-badge {{
      font-weight: 700;
      font-size: calc(1.05rem * var(--font-scale));
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
      font-size: calc(1.35rem * var(--font-scale));
      line-height: 2.3;
      font-weight: 500;
      color: #0f172a;
      margin-bottom: 8px;
      word-break: keep-all;
      overflow-wrap: break-word;
    }}

    .sentence-pron {{
      font-size: calc(1.0rem * var(--font-scale));
      color: #d97706;
      margin-bottom: 6px;
      line-height: 1.5;
    }}

    .sentence-ko {{
      font-size: calc(1.05rem * var(--font-scale));
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
      font-size: 0.85rem;
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
      font-size: calc(0.92rem * var(--font-scale));
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
      .speaker-tag {{
        width: 55px;
      }}
      .dialogue-paper {{
        padding: 12px 10px;
      }}
    }}

    /* 
      하단 미니 플레이어 바 (가림 최소화 및 닫기 버튼 제공)
    */
    .audio-dock {{
      position: fixed;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(8px);
      color: #f8fafc;
      padding: 6px 14px;
      border-radius: 30px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
      z-index: 1000;
      display: flex;
      align-items: center;
      gap: 8px;
      max-width: 95%;
      border: 1px solid rgba(255,255,255,0.15);
      transition: opacity 0.2s, transform 0.2s;
    }}

    .audio-dock.hidden {{
      opacity: 0;
      pointer-events: none;
      transform: translate(-50%, 40px);
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
      padding: 5px;
      border-radius: 50%;
    }}

    .audio-dock .now-playing-info {{
      font-size: 0.8rem;
      max-width: 170px;
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
      padding: 2px 5px;
      border-radius: 4px;
      font-size: 0.75rem;
      cursor: pointer;
    }}

    .audio-dock-close {{
      color: #94a3b8 !important;
      font-size: 0.85rem !important;
      margin-left: 4px;
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

  <!-- 
    상단 헤더 (position: relative 적용으로 핀치 줌 및 스크롤 시 본문을 절대 가리지 않음) 
  -->
  <header class="app-header">
    <div class="header-inner">
      <div class="header-title-bar">
        <h1>
          <span>제2과 구로몬 시장(黒門市場) 회화</span>
          <span class="badge">학습노트</span>
        </h1>
        <div class="btn-group">
          <button class="btn btn-sm btn-success" onclick="downloadCurrentHtml()" title="오프라인 저장용 파일 다운로드">📥 파일저장</button>
          <button class="btn btn-sm" onclick="toggleExtraSettings()" id="settingsToggleBtn">⚙️ 학습설정</button>
        </div>
      </div>
      
      <!-- 기본 1단 툴바: 탭 전환 및 전체 듣기 -->
      <div class="toolbar-row">
        <div class="btn-group">
          <button class="btn btn-primary active" id="tabBtn1" onclick="switchTab('tab1')">📖 원문 보기</button>
          <button class="btn" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 분석</button>
        </div>
        <div class="btn-group">
          <button class="btn btn-primary" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체연속듣기</button>
          <button class="btn" onclick="stopAudio()">⏹</button>
        </div>
      </div>

      <!-- 접이식 상세 설정 패널 (필요할 때만 열어서 조절) -->
      <div id="extraSettingsPanel">
        <div class="settings-subrow">
          <span class="settings-label">글자 크기:</span>
          <button class="btn btn-sm active" id="fontNormalBtn" onclick="setFontScale('normal')">보통</button>
          <button class="btn btn-sm" id="fontLargeBtn" onclick="setFontScale('large')">크게</button>
          <button class="btn btn-sm" id="fontXLargeBtn" onclick="setFontScale('xlarge')">아주크게</button>
        </div>
        <div class="settings-subrow">
          <span class="settings-label">가리기:</span>
          <button class="btn btn-sm" id="btnToggleRuby" onclick="toggleRuby()">후리가나</button>
          <button class="btn btn-sm" id="btnTogglePron" onclick="togglePron()">발음</button>
          <button class="btn btn-sm" id="btnToggleTrans" onclick="toggleTrans()">해석</button>
        </div>
        <div class="settings-subrow">
          <span class="settings-label">재생 배속:</span>
          <button class="btn btn-sm" onclick="setSpeed(0.8)">0.8x</button>
          <button class="btn btn-sm active" id="speed10" onclick="setSpeed(1.0)">1.0x</button>
          <button class="btn btn-sm" onclick="setSpeed(1.2)">1.2x</button>
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- TAB 1: FULL DIALOGUE -->
    <div id="tab1" class="view-content active">
      <div class="dialogue-paper">
        <div class="paper-header">
          <h2>会話文 (제2과 회화문 원문)</h2>
          <div class="sub">문장을 터치하거나 왼쪽 [▶] 버튼을 누르면 해당 문장 음성이 바로 재생됩니다.</div>
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
  <div class="audio-dock" id="audioDock">
    <button id="dockPlayBtn" onclick="togglePlayAll()" title="재생/일시정지">▶</button>
    <button onclick="stopAudio()" title="정지">⏹</button>
    <div class="now-playing-info" id="dockInfo">
      대화 터치 시 재생
    </div>
    <select id="dockSpeed" onchange="setSpeed(parseFloat(this.value))">
      <option value="0.8">0.8x</option>
      <option value="1.0" selected>1.0x</option>
      <option value="1.2">1.2x</option>
    </select>
    <button class="audio-dock-close" onclick="closeAudioDock()" title="닫기">✕</button>
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
    const audioDock = document.getElementById('audioDock');

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

    // 상세 설정 토글
    function toggleExtraSettings() {{
      const panel = document.getElementById('extraSettingsPanel');
      const btn = document.getElementById('settingsToggleBtn');
      panel.classList.toggle('open');
      btn.classList.toggle('active', panel.classList.contains('open'));
    }}

    function closeAudioDock() {{
      audioDock.classList.add('hidden');
    }}

    function showAudioDock() {{
      audioDock.classList.remove('hidden');
    }}

    // 파일 다운로드 기능
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
      showAudioDock();
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
      showAudioDock();
      if (isPlayingAll) {{
        audio.pause();
        isPlayingAll = false;
        dockPlayBtn.innerText = '▶';
        btnPlayAll.innerText = '▶ 전체연속듣기';
        dockInfo.innerText = '일시 정지됨';
      }} else {{
        stopAudio();
        isPlayingAll = true;
        dockPlayBtn.innerText = '⏸';
        btnPlayAll.innerText = '⏸ 일시정지';
        dockInfo.innerText = '전체 재생 중...';
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
      btnPlayAll.innerText = '▶ 전체연속듣기';
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
      document.querySelectorAll('#extraSettingsPanel button').forEach(b => {{
        if (b.innerText.includes(rate + 'x')) {{
          b.classList.add('active');
        }} else if (b.innerText.includes('x')) {{
          b.classList.remove('active');
        }}
      }});
    }}

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
  </script>
</body>
</html>
'''

# Update in all locations
paths = [
    '/Users/kwangyulllee/.gemini/antigravity/scratch/japanese_study/index.html',
    '/Users/kwangyulllee/Desktop/일본어/일본어활용1/제2과_구로몬시장_인터랙티브_학습노트.html',
    '/Users/kwangyulllee/Desktop/일본어/제2과_구로몬시장_인터랙티브_학습노트.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Updated with relative positioning and slim collapsible controls!")
