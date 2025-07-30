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

# 이미지 경로를 base64로 치환
html1 = html1.replace('src="./images/galaxy example.jpg"', f'src="{img_to_base64("images/galaxy example.jpg")}"')
html1 = html1.replace('src="./images/galaxy algorithm.jpg"', f'src="{img_to_base64("images/galaxy algorithm.jpg")}"')

html2 = html2.replace('src="./images/beaver earthquake.jpg"', f'src="{img_to_base64("images/beaver earthquake.jpg")}"')
html2 = html2.replace('src="./images/earthquake graph.jpg"', f'src="{img_to_base64("images/earthquake graph.jpg")}"')

# 출력
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content: galaxy.html'):
        htmlviewer.html(html1, height=1900)
    with st.expander('Content: earthquake.html'):
        htmlviewer.html(html2, height=1500)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by Haemin', unsafe_allow_html=True)


