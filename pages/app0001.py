import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# ------------------------------
# 데이터
# ------------------------------
co2_data = [
    {'년월': '199901', '안면도': 373.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199902', '안면도': 374.0, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199903', '안면도': 372.9, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199904', '안면도': 373.6, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199905', '안면도': 370.8, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199906', '안면도': 366.3, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199907', '안면도': 365.4, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199908', '안면도': 361.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199909', '안면도': 361.9, '고산': None, '울릉도': None, '독도': None},
    {'년월': '199912', '안면도': 371.3, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200001', '안면도': 375.0, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200002', '안면도': 375.4, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200003', '안면도': 375.4, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200005', '안면도': 372.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200006', '안면도': 369.6, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200007', '안면도': 368.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200008', '안면도': 367.2, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200009', '안면도': 365.8, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200012', '안면도': 375.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200106', '안면도': 377.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200206', '안면도': 380.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200306', '안면도': 385.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200406', '안면도': 382.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200506', '안면도': 380.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200606', '안면도': 385.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200706', '안면도': 385.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200806', '안면도': 389.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '200906', '안면도': 390.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201006', '안면도': 388.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201106', '안면도': 392.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201206', '안면도': 398.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201306', '안면도': 401.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201406', '안면도': 399.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201506', '안면도': 400.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201606', '안면도': 406.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201706', '안면도': 407.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201806', '안면도': 411.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '201906', '안면도': 410.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '202006', '안면도': 417.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '202106', '안면도': 415.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '202206', '안면도': 420.7, '고산': None, '울릉도': None, '독도': None},
    {'년월': '202306', '안면도': 427.4, '고산': 424.7, '울릉도': 423.0, '독도': 421.9},
    {'년월': '202307', '안면도': 424.6, '고산': 422.6, '울릉도': 422.0, '독도': 422.3},
    {'년월': '202308', '안면도': 418.2, '고산': 419.8, '울릉도': 420.4, '독도': 421.8},
    {'년월': '202309', '안면도': 420.0, '고산': 420.2, '울릉도': 419.2, '독도': 419.4},
    {'년월': '202310', '안면도': 426.4, '고산': 424.6, '울릉도': 424.3, '독도': None},
    {'년월': '202311', '안면도': 429.7, '고산': 427.6, '울릉도': 428.0, '독도': None},
    {'년월': '202312', '안면도': 433.7, '고산': 430.4, '울릉도': 429.3, '독도': None}
]

# 관측소 위치 데이터
locations = {
    '안면도': {'lat': 36.5381, 'lon': 126.3311},
    '고산': {'lat': 33.2933, 'lon': 126.162},
    '울릉도': {'lat': 37.4812, 'lon': 130.8986},
    '독도': {'lat': 37.2422, 'lon': 131.8622}
}
map_data = pd.DataFrame(locations).T

# ------------------------------
# 데이터 전처리 및 모델 학습 (수정 없음)
# ------------------------------
df = pd.DataFrame(co2_data)
df['년월'] = pd.to_datetime(df['년월'], format='%Y%m')
df['안면도'] = df['안면도'].interpolate(method='linear')
df_long = df.melt(id_vars='년월',
                  value_vars=['안면도', '고산', '울릉도', '독도'],
                  var_name='지역',
                  value_name='CO2 농도(ppm)')
df_long.dropna(inplace=True)
df_long['구분'] = '과거 데이터'

models = {}
for loc in df_long['지역'].unique():
    loc_df = df_long[df_long['지역'] == loc]
    X = loc_df['년월'].map(datetime.datetime.toordinal).values.reshape(-1, 1)
    Y = loc_df['CO2 농도(ppm)'].values
    model = LinearRegression()
    model.fit(X, Y)
    models[loc] = model

@st.cache_data
def generate_future_data(_models):
    future_data_all_scenarios = pd.DataFrame()
    last_date = df_long['년월'].max()
    future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=50 * 12, freq='MS')
    future_dates_ordinal_np = np.array([d.toordinal() for d in future_dates])
    scenarios = {"현재 추세 유지": 1.0, "10% 빠른 증가": 1.1, "10% 느린 증가": 0.9}
    for scenario_name, factor in scenarios.items():
        for loc, model in _models.items():
            original_slope = model.coef_[0]
            predicted_values = model.intercept_ + (original_slope * factor) * future_dates_ordinal_np
            temp_df = pd.DataFrame({
                '년월': future_dates, '지역': loc, 'CO2 농도(ppm)': predicted_values,
                '시나리오': scenario_name, '구분': f'미래 예측 ({scenario_name})'
            })
            future_data_all_scenarios = pd.concat([future_data_all_scenarios, temp_df])
    return future_data_all_scenarios

future_df_all = generate_future_data(models)

# ------------------------------
# Streamlit 웹앱 구현
# ------------------------------
st.title('🌏국내 CO₂ 농도 변화 예측 및 탄소 배출 감소 실천 다짐하기')
st.divider()

# --- 데이터 시각화 및 예측 섹션 ---
st.header('📈 CO₂ 농도 현황 및 미래 예측')

st.markdown("데이터를 통해 현재까지의 이산화탄소 농도 변화를 확인하고, 미래 예측 시나리오에 따른 변화를 탐색해 봅시다.")

st.subheader('📍 관측소 위치')
st.map(map_data, zoom=5)

st.subheader('📊 월별 CO₂ 농도 그래프')
location_options = df_long['지역'].unique()
selected_locations = st.multiselect('지역 선택 (다중 가능)', location_options, default=location_options)
scenario_choice = st.selectbox('미래 예측 시나리오 선택', options=["예측 안함"] + list(future_df_all['시나리오'].unique()))
min_date_allowed = df_long['년월'].min().to_pydatetime()
max_date_allowed = future_df_all['년월'].max().to_pydatetime() if scenario_choice != "예측 안함" else df_long['년월'].max().to_pydatetime()
default_start_date = datetime.date(2023, 1, 1) if scenario_choice != "예측 안함" else min_date_allowed
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input('시작일', default_start_date, min_value=min_date_allowed, max_value=max_date_allowed)
with col2:
    end_date = st.date_input('종료일', max_date_allowed, min_value=min_date_allowed, max_value=max_date_allowed)

if start_date > end_date:
    st.error('오류: 시작일은 종료일보다 이전 날짜여야 합니다.')
else:
    combined_df = df_long.copy()
    if scenario_choice != "예측 안함":
        selected_future_df = future_df_all[future_df_all['시나리오'] == scenario_choice]
        combined_df = pd.concat([combined_df, selected_future_df])
    mask = ((combined_df['년월'] >= pd.to_datetime(start_date)) & (combined_df['년월'] <= pd.to_datetime(end_date)) & (combined_df['지역'].isin(selected_locations)))
    final_df = combined_df[mask]
    if not final_df.empty:
        fig = px.line(
            final_df, x='년월', y='CO2 농도(ppm)', color='지역', line_dash='구분',
            title='선택된 기간 및 지역의 CO₂ 농도', labels={'년월': '연도', 'CO2 농도(ppm)': 'CO₂ 농도 (ppm)', '구분': '데이터 종류'}, markers=False)
        fig.update_layout(xaxis_title='관측 시점', yaxis_title='이산화탄소 농도 (ppm)', legend_title='범례')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning('선택된 조건에 해당하는 데이터가 없습니다.')

# [수정] 데이터 출처 명시 및 표 보기
st.markdown("""
<div style="text-align: right;">
    데이터 출처: <a href="http://www.climate.go.kr/home/09_monitoring/index.php/main" target="_blank">기상청 기후정보포털</a><br>
    <span style="font-size: 0.9em; color: #888;">혹시 필요할 경우, 웹페이지 탐색을 권장합니다.</span>
</div>
""", unsafe_allow_html=True)

if st.checkbox('보간 처리된 원본 데이터 표로 보기'):
    st.header('📜 전체 데이터 표 (안면도 보간 처리 완료)')
    display_df = df.set_index('년월')
    st.dataframe(display_df.style.format("{:.1f}", na_rep="-").format_index(lambda t: t.strftime('%Y-%m')))

st.divider()

# --- 탄소 배출 감소를 위한 실천 활동 섹션 ---
st.header("🌱 탄소 배출 감소를 위한 나의 다짐")
st.markdown("데이터를 통해 문제의 심각성을 확인했다면, 이제 우리가 할 수 있는 일들을 고민하고 실천해 봅시다.")

st.subheader("활동 1: 내가 할 수 있는 일은 무엇일까?")
st.text_area("일상생활에서 대기 중 이산화탄소 농도를 줄이기 위해 내가 실천할 수 있는 활동들을 자유롭게 적어보세요.", height=150, key="activity1")

st.subheader("활동 2: 영상으로 알아보는 탄소 중립")
with st.expander("🎥 '우리가 탄소중립을 해야 하는 진짜 이유' 영상 보기 (클릭하여 펼치기)"):
    st.video("https://youtu.be/XVAoQ60yAZc?si=DnK6y0_QGSWuyQlYhttps://youtu.be/XVAoQ60yAZc?si=DnK6y0_QGSWuyQlY")

st.subheader("활동 3: 🤖 AI 전문가와 함께 나의 생활습관 분석하기")
st.markdown("아래 프롬프트를 복사하여 **ChatGPT**와 같은 AI 챗봇에게 질문해 보세요. AI 환경 전문가가 당신의 생활 습관을 분석하고, 탄소 배출을 줄일 수 있는 구체적이고 실천 가능한 맞춤형 다짐을 세우는 데 도움을 줄 것입니다.")
st.link_button("ChatGPT와 대화 시작하기", "https://chat.openai.com/")
prompt_plan = """
당신은 개인의 탄소 발자국 분석을 전문으로 하는 뛰어난 환경 전문가입니다. 
당신의 목표는 사용자인 저의 일상생활 패턴을 분석하고, 탄소 배출을 줄이기 위한 개인 맞춤형 실천 계획을 수립하도록 돕는 것입니다.

지금부터 저와의 대화를 주도해 주세요. 
저의 생활 습관을 파악하기 위해 아래 분야에 대해 한 번에 하나씩 질문해 주세요.
1. 교통수단 (출퇴근, 이동 시 주로 이용하는 것)
2. 식습관 (육류 섭취 빈도, 배달 음식 등)
3. 에너지 사용 (전기, 난방 등)
4. 소비 습관 (물건 구매, 재활용 등)

모든 답변을 들은 후, 저의 핵심적인 탄소 배출 습관을 요약하고, 제가 꾸준히 실천할 수 있는 구체적인 '탄소 배출 감소 실천 다짐' 3가지를 함께 만들어주세요.
과정 내내 격려하며, 현실적이고 긍정적인 태도를 유지해 주세요. 이제 첫 번째 질문부터 시작해 주세요.
"""
st.code(prompt_plan, language='text')

st.subheader("활동 4: ✍️ 나의 최종 실천 다짐 기록하기")
st.text_area("AI 전문가와 논의하여 수립한 최종 실천 다짐을 이곳에 기록하고 정리해 보세요.", height=200, key="activity4")

st.subheader("활동 5: 🧑‍🏫 AI 전문가에게 나의 다짐 평가받기")
st.markdown("위에서 작성한 당신의 다짐이 얼마나 효과적이고 지속 가능한지 AI 전문가에게 평가받아 봅시다. 아래 프롬프트를 복사하고, **[여기에 자신의 다짐을 붙여넣으세요]** 부분에 위에서 작성한 자신의 다짐을 채워 넣어 질문해 보세요.")
st.link_button("ChatGPT에 다짐 평가 요청하기", "https://chat.openai.com/")
prompt_evaluate = """
당신은 환경 및 행동 심리 전문가입니다. 저는 당신의 도움을 받아 아래와 같은 '탄소 배출 감소 실천 다짐'을 세웠습니다.

[여기에 자신의 다짐을 붙여넣으세요]

위 다짐에 대해 다음 세 가지 기준에 따라 각각 100점 만점으로 평가하고, 구체적인 피드백과 개선을 위한 조언을 해주세요.
1. 지속성: 이 다짐이 얼마나 현실적이고 꾸준히 실천 가능한가?
2. 효과성: 실제로 저의 탄소 발자국을 줄이는 데 얼마나 효과적인가?
3. 영향력: 주변 사람들에게 긍정적인 영향을 미칠 잠재력이 있는가?
"""
st.code(prompt_evaluate, language='text')

# [추가] 활동 6: AI의 평가 내용 기록하기
st.subheader("활동 6: 📋 AI의 평가 내용 기록하기")
st.text_area("AI 전문가에게 평가받은 내용을 이곳에 옮겨 적어보세요.", height=200, key="activity6")

st.divider()

# [추가] 활동 내용 제출 기능
st.header("✉️ 활동 내용 제출하기")
if st.button("교사에게 제출하기"):
    # session_state에서 각 활동 내용 가져오기
    activity1_text = st.session_state.get("activity1", "작성된 내용이 없습니다.")
    activity4_text = st.session_state.get("activity4", "작성된 내용이 없습니다.")
    activity6_text = st.session_state.get("activity6", "작성된 내용이 없습니다.")
    
    # 제출할 텍스트 파일 내용 구성
    submission_text = f"""
--- 학생 활동 결과 보고서 ---

[활동 1: 내가 할 수 있는 일은 무엇일까?]
{activity1_text}

----------------------------------------

[활동 4: 나의 최종 실천 다짐 기록하기]
{activity4_text}

----------------------------------------

[활동 6: AI의 평가 내용 기록하기]
{activity6_text}
"""
    st.success("제출 내용이 준비되었습니다! 아래 버튼을 눌러 텍스트 파일을 다운로드한 후, 선생님께 이메일로 제출해주세요.")
    
    # 다운로드 버튼 생성
    st.download_button(
        label="활동 내용 다운로드",
        data=submission_text.encode('utf-8'), # 한글이 깨지지 않도록 utf-8로 인코딩
        file_name="탄소중립_실천다짐_활동보고서.txt",
        mime="text/plain"
    )