import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
n_points = 100
df = pd.DataFrame({
    'x' : np.random.rand(n_points),
    'y' : np.random.rand(n_points),
    'frame' : np.repeat(np.arange(1,11),n_points//10),
    'category' : np.random.choice(['a','b','c'], n_points)
})


fig = px.scatter(
    df,
    x = 'x',
    y = 'y',
    color='category',
    animation_frame = 'frame',
    animation_group='category',
    title = 'Animated Scatter Plot with Longer Data'
)

st.plotly_chart(fig)

st.write('이 그래프는 시간에 따라 변화하는 데이터를 보여줍니다.\
         각 프레임은 다른 시점을 나타냅니다.')