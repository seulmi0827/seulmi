import streamlit as st


def history_printer():
    for chat in st.session_state['chat_history']:
            if chat['role'] == 'user':
                with st.chat_message(chat['role']):
                    st.write(chat['content'])
            elif chat['role'] == 'ai':
                with st.chat_message(chat['role']):
                    st.write(chat['content'])