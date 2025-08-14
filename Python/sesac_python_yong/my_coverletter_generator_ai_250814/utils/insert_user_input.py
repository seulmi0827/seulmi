import streamlit as st
from ai.revise_cover_letter_llm import revise_cover_letter_llm

def insert_user_input(status_placeholder, user_input):
    if st.session_state['chat_history']:
        # 6단계: 자소서 수정
        status_placeholder.info("🔧 자소서 수정 및 평가 중...")
        my_revise_request = user_input
        
        if not st.session_state['my_revised_cover_letter']:
            my_revised_cover_letter = revise_cover_letter_llm(my_revise_request, 
                                                            st.session_state['my_cover_letter'][-1], 
                                                            st.session_state['recruit_info'][-1], 
                                                            st.session_state['corp_info'][-1])
        else:
            my_revised_cover_letter = revise_cover_letter_llm(my_revise_request, 
                                                            st.session_state['my_revised_cover_letter'][-1], 
                                                            st.session_state['recruit_info'][-1], 
                                                            st.session_state['corp_info'][-1])
        st.session_state['my_revise_request'].append(my_revise_request)
        st.session_state['chat_history'].append({'role':'user','content':user_input})
        
        st.session_state['my_revised_cover_letter'].append(my_revised_cover_letter)
        st.session_state['chat_history'].append({'role':'ai','content':my_revised_cover_letter['revised']})
        status_placeholder.info("✅ 결과 출력 완료!")
        