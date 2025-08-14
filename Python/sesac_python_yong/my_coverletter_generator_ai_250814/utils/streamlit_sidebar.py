import streamlit as st
from db.get_connection import get_connection
from db.get_db import get_all_sessions, get_all_corp_names, get_all_corp_ids
from db.save_db import save_session, save_chat
from utils.streamlit_layout import create_st_session_state
from utils.streamlit_layout import streamlit_layout

def streamlit_side_bar():
    with st.sidebar:
        agree = st.checkbox("대화 기록을 db에 저장", value=False)
        init_conversation = st.button('세션 초기화 및 저장')
        try:
            conn = get_connection()
            conn.close()
            st.sidebar.success("✅ DB 연결 완료!")

            # 세션 목록 불러오기
            sessions = get_all_sessions()
            st.session_state['session_id'] = sessions
            if sessions:
                st.sidebar.write("📂 저장된 세션 ID:")
                st.sidebar.write(", ".join(map(str, sessions)))
            else:
                st.sidebar.info("현재 저장된 세션이 없습니다.")
                
            corps = get_all_corp_names()
            cor_name_ids = get_all_corp_ids()
            st.session_state['corp_name_id'] = cor_name_ids
            if corps:
                st.sidebar.write("📂 저장된 기업 List:")
                st.sidebar.write(", ".join(map(str, corps)))
            else:
                st.sidebar.info("현재 저장된 기업이 없습니다.")
                    
        except Exception as e:
            st.sidebar.error(f"❌ DB 연결 실패: {e}")
            

    if init_conversation:
        save_session()
        if agree:
            save_chat(st.session_state['session_id'][-1], st.session_state['corp_name'][-1])
            st.sidebar.text('db에 저장완료!')
            
                    # 세션 상태 초기화
            st.session_state.clear()  # 모든 session_state 초기화

            # 페이지 다시 실행
            st.rerun()
