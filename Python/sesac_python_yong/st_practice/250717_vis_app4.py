import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x' : [1,2,3,4,5],
    'y' : [10,11,12,13,14],
    'z' : [5,4,3,2,1],
    'category' : ['a','v','a','v','a']
})

fig = px.scatter_3d(df, x='x',y = 'y', z = 'z',
color = 'category', title='3D scatter Plot')

st.plotly_chart(fig)