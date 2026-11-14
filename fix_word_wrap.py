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
    /*
      [핵심 수정: 긴 문장 자동 줄바꿈 & 반응형 최적화]
      1. word-break: break-all + overflow-wrap: anywhere 
         -> 일본어/한국어가 절대 화면 밖이나 카드 오른쪽으로 튀어나가지 않고 100% 자동 줄바꿈!
      2. 100% 완전 단일 순백색(#ffffff) 일체형 배경 -> 좌우 색상 분리 원천 차단
      3. position: static 헤더 -> 본문과 한 덩어리로 같이 스크롤/확대
      4. 모바일 화면 폭 100% 풀 반응형 레이아웃
    */
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --ruby-color: #1d4ed8;
      --text-main: #0f172a;
      --text-sub: #475569;
      --border-line: #e2e8f0;
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
      overflow-x: hidden; /* 가로 스크롤 완전 방지 */
    }}

    /* 모든 텍스트 강제 자동 줄바꿈 (옆으로 튀어나감 완전 해결) */
    .dialogue-text, 
    .card-japanese, 
    .card-pron, 
    .card-ko, 
    .jp-line,
    .details-box ul li {{
      word-break: break-all !important;
      overflow-wrap: anywhere !important;
      word-wrap: break-word !important;
      white-space: normal !important;
    }}

    /* 문서 일체형 헤더 (스크롤/확대 시 본문과 같이 한 덩어리로 움직임) */
    header.paper-header {{
      width: 100%;
      background: #ffffff;
      border-bottom: 2px solid #0f172a;
      padding: 14px 12px 10px 12px;
      max-width: 800px;
      margin: 0 auto;
    }}

    .title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 10px;
    }}

    .title-row h1 {{
      font-size: calc(1.2rem * var(--font-scale));
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .title-row .badge {{
      background: #e0e7ff;
      color: #3730a3;
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 9999px;
      font-weight: 600;
    }}

    /* 초슬림 반응형 툴바 */
    .toolbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 6px;
      background: #f8fafc;
      padding: 8px 10px;
      border-radius: 8px;
      border: 1px solid var(--border-line);
    }}

    .btn-group {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-wrap: wrap;
    }}

    button.btn, a.btn {{
      font-family: inherit;
      font-size: 0.82rem;
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 600;
      white-space: nowrap;
      text-decoration: none;
      transition: all 0.1s;
      -webkit-tap-highlight-color: transparent;
    }}

    button.btn:active, a.btn:active {{
      background: #e2e8f0;
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

    button.btn-success {{
      background: #059669;
      color: white;
      border-color: #059669;
    }}

    button.btn-sm {{
      padding: 4px 7px;
      font-size: 0.75rem;
    }}

    /* 일체형 플레이어 바 (헤더 바로 아래 착 붙음) */
    .integrated-player-bar {{
      width: 100%;
      max-width: 800px;
      margin: 8px auto 0 auto;
      padding: 8px 10px;
      background: #0f172a;
      color: #ffffff;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .player-left {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .player-play-btn {{
      background: #38bdf8;
      color: #0f172a;
      border: none;
      padding: 5px 12px;
      border-radius: 5px;
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
    }}

    .player-stop-btn {{
      background: #334155;
      color: white;
      border: none;
      padding: 5px 8px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 0.82rem;
    }}

    .now-playing-text {{
      font-size: 0.78rem;
      color: #94a3b8;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 200px;
    }}

    .now-playing-text strong {{
      color: #38bdf8;
    }}

    .speed-select {{
      background: #334155;
      color: white;
      border: 1px solid #475569;
      padding: 4px 6px;
      border-radius: 5px;
      font-size: 0.75rem;
      cursor: pointer;
    }}

    /* 본문 영역 */
    main.document-body {{
      width: 100%;
      max-width: 800px;
      margin: 12px auto;
      padding: 0 10px 60px 10px;
      background: #ffffff !important;
    }}

    /* 요미가나(루비) */
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

    /* 탭 1: 원문 대화 목록 */
    .view-content {{
      display: none;
    }}
    .view-content.active {{
      display: block;
    }}

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
      width: 60px;
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

    /* 탭 2: 문장별 상세 분석 (화면 꽉 채우는 카드형 & 튀어나감 원천 방지) */
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
      overflow: hidden; /* 테두리 밖 넘침 방지 */
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
        width: 52px;
      }}
      main.document-body {{
        padding: 0 8px 60px 8px;
      }}
    }}
  </style>
</head>
<body>

  <!-- 문서 일체형 헤더 (고정 없음, 문서와 함께 100% 동일 비율 확대) -->
  <header class="paper-header">
    <div class="title-row">
      <h1>
        <span>第2課 黒門市場 (제2과 구로몬 시장)</span>
        <span class="badge">인터랙티브 회화</span>
      </h1>
      <button class="btn btn-sm btn-success" onclick="downloadHtmlFile()" title="오프라인 저장용 파일 다운로드">📥 파일 저장</button>
    </div>

    <!-- 심플 반응형 툴바 -->
    <div class="toolbar">
      <div class="btn-group">
        <button class="btn btn-primary active" id="tabBtn1" onclick="switchTab('tab1')">📖 원문 보기</button>
        <button class="btn" id="tabBtn2" onclick="switchTab('tab2')">🔍 문장별 분석</button>
      </div>
      <div class="btn-group">
        <button class="btn btn-sm active" id="fontNormalBtn" onclick="setFontScale('normal')">보통</button>
        <button class="btn btn-sm" id="fontLargeBtn" onclick="setFontScale('large')">크게</button>
        <button class="btn btn-sm" id="fontXLargeBtn" onclick="setFontScale('xlarge')">아주크게</button>
        <button class="btn btn-sm" id="btnToggleRuby" onclick="toggleRuby()">후리가나</button>
      </div>
    </div>

    <!-- 일체형 플레이어 바 (헤더 바로 아래 위치) -->
    <div class="integrated-player-bar">
      <div class="player-left">
        <button class="player-play-btn" id="btnPlayAll" onclick="togglePlayAll()">▶ 전체연속듣기</button>
        <button class="player-stop-btn" onclick="stopAudio()">⏹ 정지</button>
      </div>
      <div class="now-playing-text" id="nowPlayingText">
        문장을 터치하면 해당 음성이 재생됩니다.
      </div>
      <div>
        <select class="speed-select" id="speedSelect" onchange="setSpeed(parseFloat(this.value))">
          <option value="0.8">0.8x</option>
          <option value="1.0" selected>1.0x</option>
          <option value="1.2">1.2x</option>
        </select>
      </div>
    </div>
  </header>

  <!-- 문서 본문 (순백색 일체형 배경) -->
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
          <button class="btn btn-primary btn-sm" onclick="playSentence({d['id']}, {d['start']}, {d['end']})">▶ 1회 듣기</button>
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
      document.getElementById('tabBtn1').classList.toggle('active', tabId === 'tab1');
      document.getElementById('tabBtn2').classList.toggle('active', tabId === 'tab2');
    }}

    // 문장 재생
    function playSentence(id, start, end) {{
      stopAudio();
      currentSentenceId = id;
      const d = dialogues.find(x => x.id === id);
      highlightSentence(id);
      
      nowPlayingText.innerHTML = `<strong>${{d.speaker.split()[0]}}</strong>: ${{d.jp_plain}}`;

      audio.currentTime = start;
      const p = audio.play();
      if (p !== undefined) p.catch(() => {{}});

      const duration = (end - start) * 1000 / audio.playbackRate;
      sentenceTimeout = setTimeout(() => {{
        audio.pause();
        stopHighlight();
        nowPlayingText.innerText = '재생 완료';
      }}, duration);
    }}

    // 전체 재생 토글
    function togglePlayAll() {{
      if (isPlayingAll) {{
        audio.pause();
        isPlayingAll = false;
        btnPlayAll.innerText = '▶ 전체연속듣기';
        nowPlayingText.innerText = '일시 정지됨';
      }} else {{
        stopAudio();
        isPlayingAll = true;
        btnPlayAll.innerText = '⏸ 일시정지';
        nowPlayingText.innerText = '전체 연속 재생 중...';
        audio.currentTime = 0;
        audio.play().catch(() => {{}});
      }}
    }}

    audio.addEventListener('timeupdate', () => {{
      if (isPlayingAll) {{
        const cur = audio.currentTime;
        const currentD = dialogues.find(d => cur >= d.start && cur < d.end);
        if (currentD && currentD.id !== currentSentenceId) {{
          currentSentenceId = currentD.id;
          highlightSentence(currentD.id);
          nowPlayingText.innerHTML = `<strong>${{currentD.speaker.split()[0]}}</strong>: ${{currentD.jp_plain}}`;
        }}
      }}
    }});

    audio.addEventListener('ended', () => {{
      stopAudio();
      nowPlayingText.innerText = '전체 재생 완료';
    }});

    function stopAudio() {{
      if (sentenceTimeout) {{
        clearTimeout(sentenceTimeout);
        sentenceTimeout = null;
      }}
      audio.pause();
      isPlayingAll = false;
      stopHighlight();
      btnPlayAll.innerText = '▶ 전체연속듣기';
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

    function toggleRuby() {{
      document.body.classList.toggle('hide-ruby');
      const isHidden = document.body.classList.contains('hide-ruby');
      document.getElementById('btnToggleRuby').classList.toggle('active', isHidden);
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

print("Updated with word-break: break-all & auto-wrap for all Japanese sentences!")
