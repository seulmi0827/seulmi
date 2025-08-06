import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import time
from langchain_core.prompts import load_prompt



###############
###streamlit###
###############

with st.sidebar:
    init_conversation = st.button('대화 초기화')
    select_value = st.selectbox('사용 목적에 맞는 프롬프트를 선택하세요.',['기본','sns게시글','요약'])
    
st.title('나의 챗봇')

if init_conversation:
    st.session_state = {}
    st.session_state['chat_history'] = []

user_input = st.chat_input()




###############
### chat_bot###
###############

# OPEN AI API 키 설정
load_dotenv()


# ChatOpenAI 모델을 초기화합니다.
model = ChatOpenAI()

# 대화형 프롬프트를 생성합니다. 이 프롬프트는 시스템 메시지, 이전 대화 내역, 그리고 사용자 입력을 포함합니다.
sns_system_prompt = load_prompt(r"only-pull-me\5_생성형AI\실습\post_sns.yaml",encoding='utf-8')
summary_system_prompt = load_prompt(r"only-pull-me\5_생성형AI\실습\summary.yaml",encoding='utf-8')

if select_value == '기본':
    selected_prompt = "You are a helpful chatbot"
elif select_value =="sns게시글":
    selected_prompt = sns_system_prompt.format(question=user_input)
elif select_value == '요약':
    selected_prompt = summary_system_prompt.format(question=user_input)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", selected_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt | model

ai_answer = chain.invoke({"input":user_input,"chat_history":st.session_state['chat_history']}).content


if user_input:
    st.session_state['chat_history'].append({'role':'user','content':user_input})
    if ai_answer:
        st.session_state['chat_history'].append({'role':'ai','content':ai_answer})

for chat in st.session_state['chat_history']:
    if chat['role'] == 'user':
        with st.chat_message(chat['role']):
            st.write(chat['content'])
    else:
        with st.chat_message(chat['role']):
            #with st.container():
            with st.empty():
                printer = ''
                for txt in chat['content']:
                    printer += txt
                    st.write(printer)
                    time.sleep(0.05)