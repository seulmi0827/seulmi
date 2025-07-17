import streamlit as st
import seaborn as sns
import pandas as pd

df = sns.load_dataset('iris')

fig = sns.pairplot(df, hue='species')

#st.pyplot(fig)