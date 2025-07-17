import pandas as pd
import streamlit as st

df = pd.DataFrame({
    '이름': ["홍길동",'이순신','강감찬','신사임당'],
    '점수':[90,85,88,99]
})
st.table(df)
st.dataframe(df)

# st.json([
#     {'이름' : '이순신', '점수':50},
#     {'이름' : '강감찬', '점수':30},
#     {'이름' : '을지문덕', '점수':90},
#     {'이름' : '신사임당', '점수':80},
    
# ])

size =3

page = st.number_input('페이지',1,(len(df)//size)+1)

st.write(f'현재 페이지 :{page}')

st.table(df.iloc[((len(df)//size)+1)*(page-1):((len(df)//size)+1)*page])
