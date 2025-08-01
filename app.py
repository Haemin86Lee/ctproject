import streamlit as st
import streamlit.components.v1 as htmlviewer
import base64

st.set_page_config(layout='wide', page_title="Haemin's Webapp!!")
st.title("It's fun Earth Science time now!!")

# Base64 변환 함수
def img_to_base64(img_path):
    with open(img_path, 'rb') as f:
        return f"data:image/jpg;base64,{base64.b64encode(f.read()).decode()}"

# HTML 파일 읽기
with open('galaxy.html', 'r', encoding='utf-8') as f1:
    html1 = f1.read()
with open('earthquake.html', 'r', encoding='utf-8') as f2:
    html2 = f2.read()

html3 = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>외부 은하 분류하기 - CT 힌트</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 10px;
      background-color: #f4faff;
    }
    h1 {
      color: #003366;
    }
    .section {
      margin-bottom: 30px;
    }
    .hint-box {
      border: 2px solid #cce;
      padding: 15px;
      margin-top: 10px;
      background-color: #eef5ff;
      display: none;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #007acc;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fa3;
    }
  </style>
</head>
<body>

<h1>💫 외부 은하 분류하기 - 컴퓨팅 사고 힌트</h1>

<div class="section">
  <h2>1️⃣ 문제 분해</h2>
  <button onclick="toggleHint('hint1')">힌트 보기</button>
  <div class="hint-box" id="hint1">
    은하를 분류하려면 어떤 기준이 필요한가요? <br>
    (가), (나), (다)에 어떤 질문을 넣으면 각 은하를 나눌 수 있을지 생각해보세요. <br>
    큰 문제(은하 분류)를 작은 질문(형태, 나선팔, 막대 구조)으로 나누어 봅시다.
  </div>
</div>

<div class="section">
  <h2>2️⃣ 추상화</h2>
  <button onclick="toggleHint('hint2')">힌트 보기</button>
  <div class="hint-box" id="hint2">
    복잡한 은하의 이미지를 단순한 특징으로 표현해 보세요.<br>
    예: 타원처럼 보이는가? 팔이 있나? 팔이 중심에서 퍼지나?<br>
    핵심 요소만 추려서 비교하기 쉽게 만들어보세요.
  </div>
</div>

<div class="section">
  <h2>3️⃣ 패턴 인식</h2>
  <button onclick="toggleHint('hint3')">힌트 보기</button>
  <div class="hint-box" id="hint3">
    A~H 은하 중 규칙적인 형태를 가진 은하는 어떤 것들인가요?<br>
    나선팔이 있는 은하를 찾아보세요.<br>
    막대 구조가 있는 은하와 없는 은하는 어떻게 구분할 수 있을까요?
  </div>
</div>

<div class="section">
  <h2>4️⃣ 알고리즘 설계</h2>
  <button onclick="toggleHint('hint4')">힌트 보기</button>
  <div class="hint-box" id="hint4">
    (가) → (나) → (다) 순으로 질문을 던져보세요.<br>
    예: <br>
    (가) 형태가 규칙적인가? → No → G, H<br>
    (나) 나선팔이 있는가? → No → B, E<br>
    (다) 중심부에 막대가 있는가? → Yes → A, F / No → C, D<br>
    이처럼 흐름도를 따라 조건문을 만들면 분류가 쉬워져요!
  </div>
</div>

<script>
  function toggleHint(id) {
    const box = document.getElementById(id);
    box.style.display = box.style.display === 'block' ? 'none' : 'block';
  }
</script>

</body>
</html>
"""

html4 = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>진앙의 위치 결정 - 컴퓨팅 사고 힌트</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f0faff;
      margin: 10px;
    }
    h1 {
      color: #003366;
    }
    .section {
      margin-bottom: 25px;
    }
    .hint-box {
      display: none;
      padding: 10px;
      background-color: #eef5ff;
      border: 2px solid #ccddee;
      margin-top: 10px;
    }
    button {
      background-color: #007acc;
      color: white;
      border: none;
      padding: 10px 16px;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fa3;
    }
  </style>
</head>
<body>

<h1>🌍 진앙의 위치 결정하기 - 컴퓨팅 사고 힌트</h1>

<div class="section">
  <h2>1️⃣ 문제 분해</h2>
  <button onclick="toggleHint('hint1')">힌트 보기</button>
  <div class="hint-box" id="hint1">
    진앙을 찾는 문제를 해결하기 위해 다음과 같이 나눌 수 있어요:<br>
    - <b>PS시 계산</b><br>
    - <b>진앙까지 거리 측정</b><br>
    - <b>원 그리기 및 교차점 찾기</b>
  </div>
</div>

<div class="section">
  <h2>2️⃣ 추상화</h2>
  <button onclick="toggleHint('hint2')">힌트 보기</button>
  <div class="hint-box" id="hint2">
    복잡한 지진파 기록을 간단하게 표현해보세요:<br>
    - PS시 = S파 도착시간 - P파 도착시간<br>
    - 거리는 PS시에 비례<br>
    - 반지름 = 거리, 원의 중심 = 관측소
  </div>
</div>

<div class="section">
  <h2>3️⃣ 패턴 인식</h2>
  <button onclick="toggleHint('hint3')">힌트 보기</button>
  <div class="hint-box" id="hint3">
    - PS시가 클수록 진앙과의 거리가 멀다<br>
    - 두 개의 원은 두 점에서 교차하지만<br>
    - 세 개의 원이 만나는 <b>하나의 점</b>이 바로 진앙이다!
  </div>
</div>

<div class="section">
  <h2>4️⃣ 알고리즘 설계</h2>
  <button onclick="toggleHint('hint4')">힌트 보기</button>
  <div class="hint-box" id="hint4">
    1. 관측소 A, B, C의 PS시 구하기<br>
    2. PS시에 비례하여 거리 계산<br>
    3. 세 관측소 중심으로 반지름 원 그리기<br>
    4. 세 원의 교차점 찾기 → 진앙
  </div>
</div>

<script>
function toggleHint(id) {
  const box = document.getElementById(id);
  box.style.display = box.style.display === "block" ? "none" : "block";
}
</script>

</body>
</html>
"""

# 이미지 경로를 base64로 치환
html1 = html1.replace('src="./images/galaxy example.jpg"', f'src="{img_to_base64("images/galaxy example.jpg")}"')
html1 = html1.replace('src="./images/galaxy algorithm.jpg"', f'src="{img_to_base64("images/galaxy algorithm.jpg")}"')

html2 = html2.replace('src="./images/beaver earthquake.jpg"', f'src="{img_to_base64("images/beaver earthquake.jpg")}"')
html2 = html2.replace('src="./images/earthquake graph.jpg"', f'src="{img_to_base64("images/earthquake graph.jpg")}"')

# 출력
col1, col2 = st.columns((4,2))
with col1:
    with st.expander('Content: galaxy.html'):
        htmlviewer.html(html1, height=2000)
    with st.expander('Content: earthquake.html'):
        htmlviewer.html(html2, height=1500)

with col2:
    with st.expander('Tips..'):
        st.info('은하의 분류 기준은 크게 세 가지예요: \n1. 규칙성\n2. 나선팔 유무\n3. 중심부 구조입니다.')
        htmlviewer.html(html3, height=1400)
        
    with st.expander('Tips..'):
        st.info('지진파 도착시간 차이(PS시)는 진앙과의 거리 계산에 핵심입니다.')
        htmlviewer.html(html4, height=1200)

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Haemin', unsafe_allow_html=True)




