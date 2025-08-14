import streamlit as st


def streamlit_layout():

    st.title('자소서 생성기')

    corp_name = st.text_input('기업명',key="corp_name_input")

    recruit_info = st.text_input('채용공고 내용', key="recruit_info_input")
    
    my_request = st.text_input('자소서질문', key="my_request_input")

    generate_button = st.button('답변생성')

    user_input = st.chat_input()
 
    return corp_name, recruit_info, my_request, generate_button, user_input

def create_st_session_state():
    st.session_state['chat_history'] = []
    st.session_state['corp_name'] = []
    st.session_state['recruit_info'] = []
    st.session_state['my_request'] = []
    st.session_state['classified_type'] = []
    st.session_state['corp_info'] = []
    st.session_state['corp_intro'] = []
    st.session_state['ideal_talent'] = []
    st.session_state['main_business'] = []
    st.session_state['esg_activity'] = []
    st.session_state['my_revise_request'] = []
    st.session_state['my_cover_letter'] = []
    st.session_state['my_revised_cover_letter'] = []
    st.session_state['session_id'] = []
    