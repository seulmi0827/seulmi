import pandas as pd
import streamlit as st

st.title('hi')
st.write('bye')

with st.sidebar:
    st.title('사이드바')

v = st.button('클릭')
print(v)

cols = st.columns(2)
with cols[0]:
    st.metric('주가', '$3.7', 0.2)

with cols[1]:
    st.metric('거래량', '5.4m', -0.7)

with st.expander('상세데이터'):
    # ✅ 반드시 2차원 구조나 DataFrame이어야 함
    st.table(pd.DataFrame({'항목': ['a']}))

if v:
    st.write('버튼 클릭됨')

vol = st.slider('볼륨')
st.write(vol)

input_name = st.text_input('이름')
st.write(input_name)
