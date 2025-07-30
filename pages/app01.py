import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
st.set_page_config(page_title="CO₂ 실천 다짐 Webbapp앱", layout="wide")
st.title("🌏CO₂ Data Explorer & Personal Climate Action Planner")

# 1. 데이터 출처 안내
st.markdown("### 🌐 실시간 CO₂ 농도 정보")
st.markdown("""
현재 웹앱에서는 직접 실시간 데이터를 불러올 수 없지만, 아래 링크를 통해 최신 대기 중 이산화탄소 농도 정보를 확인할 수 있습니다:

🔗 [기후정보포털 CO₂ 농도 추이 바로가기](http://www.climate.go.kr/home/09_monitoring/ghg/co2_global_trend)
""")

# 임의 초기값
latest_co2 = 427.0
base_year = 2025
end_year = 2050
years = np.arange(base_year, end_year + 1)

# CO₂ & 온도 예측 그래프
st.markdown("### 🔮 CO₂ 배출 시나리오와 지구 평균 온도 예측")

scenario = st.selectbox("2050년까지의 이산화탄소 배출 시나리오를 선택하세요", 
                        ["현재 추세 유지", "배출률 10% 감소", "배출률 10% 증가"])

base_year = 2025
end_year = 2050
years = np.arange(base_year, end_year + 1)
latest_co2 = 427.0

growth_rates = {
    "현재 추세 유지": 2.1,
    "배출률 10% 감소": 1.89,
    "배출률 10% 증가": 2.31
}

growth_rate = growth_rates[scenario]
co2 = [latest_co2]
temps = [1.1]

for i in range(1, len(years)):
    co2.append(co2[i-1] + growth_rate)
    delta = co2[i] - 280
    temp = round(1.1 + (delta / 100) * 1.8, 2)
    temps.append(temp)

fig, ax1 = plt.subplots()
ax1.plot(years, co2, 'g-', label='CO₂ 농도 (ppm)')
ax1.set_xlabel('연도')
ax1.set_ylabel('CO₂ 농도 (ppm)', color='g')
ax1.tick_params(axis='y', labelcolor='g')

ax2 = ax1.twinx()
ax2.plot(years, temps, 'r--', label='지구 평균 온도 상승 (℃)')
ax2.set_ylabel('지구 평균 온도 상승 (℃)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

fig.tight_layout()
plt.title('2050년까지 CO₂ 및 온도 예측 시나리오')
st.pyplot(fig)

st.markdown("""
### 📊 예측 결과 요약
2050년 예상 CO₂ 농도: **{:.2f} ppm**  
2050년 예상 지구 평균 온도 상승: **{}℃**
""".format(co2[-1], temps[-1]))


# ---------------------------
st.markdown("""
---
## 🤖 실천 다짐하러 가기 (ChatGPT 연동)

아래 버튼을 클릭하면 챗GPT에서 실천 다짐을 추천받을 수 있습니다.  
먼저 ChatGPT에 다음 프롬프트를 복사해서 붙여넣어 보세요:
""")

st.code("""너는 기후 과학자이자 환경 교육 AI야.
학생이 자신의 생활습관, 진로, 환경 태도를 말하면, 
그에 맞는 탄소 감축 실천 다짐 5가지를 과학적 근거와 함께 추천해줘.
또한 그 실천이 지구와 이웃에게 어떤 긍정적 영향을 줄 수 있을지도 알려줘.

예) 나는 고등학생이고 자주 자가용을 타고, 요즘 기후 위기에 관심이 있어.
""", language="markdown")

chatgpt_url = "https://chat.openai.com/"
if st.button("🌐 챗GPT로 이동하여 실천 다짐 받기"):
    st.markdown(f"[ChatGPT 바로가기]({chatgpt_url})", unsafe_allow_html=True)


# ---------------------------
# ChatGPT로 이동해 AI 추천 받기
st.markdown("## 🤖 ChatGPT에 실천 다짐 평가받기")

st.markdown("""
👉 아래 버튼을 누르면 [ChatGPT](https://chat.openai.com/)로 이동합니다.  
아래 예시 프롬프트를 복사해 붙여넣으면 실천 다짐을 추천받을 수 있어요:
""")

st.code("""너는 기후 과학자이자 환경 교육 AI야.
내가 다짐한 일상 생활 속 이산화탄소 절감 다짐을 보고,
이러한 실천 다짐이 사회적으로 어떤 긍정적인 영향을 끼칠 수 있는지 알려줘.
추가로 내가 꾸준히 위 활동을 지속 할 수 있도록, 실천 체크리스트를 제안해줘.""", language="text")

if st.button("🌐 ChatGPT로 이동하기"):
    st.markdown("[👉 ChatGPT 바로가기](https://chat.openai.com/)", unsafe_allow_html=True)

# ---------------------------
# 체크리스트 작성
st.markdown("## ✅ 나의 실천 다짐")

st.markdown("위에서 작성한 실천 다짐과 실천 게획, 사회적 영향에 대해 정리해서 작성해보세요.")

check_items = []
for i in range(1, 6):
    item = st.text_input(f"✔ 실천 항목 {i}", key=f"check{i}")
    if item:
        check_items.append(item)

if check_items:
    st.success("🎯 나의 실천 체크리스트:")
    for i, item in enumerate(check_items, 1):
        st.markdown(f"- [ ] {item}")

# ---------------------------
st.markdown("---")
st.caption("데이터 출처: IPCC, climate.go.kr | 제작: 기후변화 대응 실천 웹앱")
