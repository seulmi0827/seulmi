import streamlit as st
import pandas as pd

cars_df = pd.read_csv('cars.csv')
mf_ls = cars_df['Manufacturer'].unique()

st.title('자동차데이터')

st.write('자동차 데이터테이블')

mf = st.selectbox("제조사", options=mf_ls)
col = st.selectbox("정렬할 칼럼 선택",cars_df.columns)
rdio = st.radio('정렬 순서 선택',['오름차순','내림차순'])

if rdio == '오름차순':
    st.table(cars_df[cars_df['Manufacturer']==mf].sort_values(col,ascending=True))
elif rdio == '내림차순':
    st.table(cars_df[cars_df['Manufacturer']==mf].sort_values(col,ascending=False))
