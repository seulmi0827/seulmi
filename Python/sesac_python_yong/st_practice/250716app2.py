import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.DataFrame({
    "x":[1,2,3,4,5],
    "y":[10,11,12,13,14],
    "category" : ['a','b','c','a','b']
})

fig = px.scatter(df, x='x',y='y',color='category',
                 title = 'plotly와 streamlit 연동 예제')

st.title('plotly 연동예제')
st.plotly_chart(fig)


st.markdown('**굵은 글자**')
st.markdown('*기울임*')
st.markdown('~취소선~')

st.title('마크다운 문법 예제')
st.write('이 앱은 다양한 마크다운 문법을 살펴보는 예제입니다.')

st.write('리스트')

st.markdown("""
- 항복 1
- 항목 2
    = 하위 항복 2.1
1. 첫 번째
2. 두 번째            
"""
)

st.write('테이블')

st.markdown("""
| 헤더 1 | 헤더 2|
|-------|-------|
| 값 1   | 값 2  |
| 값 3   | 값 4  |
""")

st.write('링크')

st.markdown('[Streamlit 공식 사이트](https://streamlit.io)')
st.write('이미지')
st.markdown('![우리집고양이](C:/Users/seul/Desktop/KakaoTalk_20250715_094140413.jpg)')

