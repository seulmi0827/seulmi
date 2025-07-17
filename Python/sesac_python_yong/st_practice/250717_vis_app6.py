import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

g = sns.FacetGrid(df,col='time',row = 'sex', margin_titles=True)
g.map(sns.scatterplot, 'total_bill', 'tip')

#st.pyplot(g)