import streamlit as st
import plotly.express as px
import pandas as pd

data = {
    'category':['a','b','c','d'],
    'values':[10,20,15,25]
}
df = pd.DataFrame(data)

fig = px.bar(df, x = 'category', y = 'values',
title = 'plotly var char example')

st.plotly_chart(fig)