import streamlit as st
from dotenv import load_dotenv
from utils.history_printer import history_printer
from utils.streamlit_layout import streamlit_layout
from utils.streamlit_sidebar import streamlit_side_bar
from utils.click_generate_button import click_generate_button
from utils.insert_user_input import insert_user_input

# 환경변수 설정
load_dotenv(r'C:\Users\seul\Desktop\yong\.env')

#스트림릿 레이아웃 설정
corp_name, recruit_info, my_request, generate_button, user_input= streamlit_layout()
streamlit_side_bar()

# 상태 표시 영역 만들기
status_placeholder = st.empty()

# 자기소개서 초안 생성
if generate_button:
    click_generate_button(corp_name, recruit_info, my_request,status_placeholder)

# 자기소개서 수정본 생성
if user_input:
    insert_user_input(status_placeholder, user_input)
    
# 대화 기록 출력
if 'my_cover_letter' in st.session_state:
    history_printer()


