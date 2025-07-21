import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

####    scatter Plot   ####
st.title('붓꽃 Data 시각화')
df = sns.load_dataset('iris')

g1 = sns.FacetGrid(df,col='species', margin_titles=True,hue='species')
g1.map(sns.scatterplot, 'sepal_length', 'sepal_width')

g2 = sns.FacetGrid(df,col='species', margin_titles=True,hue='species')
g2.map(sns.scatterplot, 'petal_length','petal_width')

st.write('종류 별 꽃받침 길이&너비')
st.pyplot(g1.figure)

st.write('종류 별 꽃잎 길이&너비')
st.pyplot(g2.figure)   


####    box Plot   ####
col_1 = st.columns(2)
with col_1[0]:
    fig = px.box(df, x="species", y="sepal_length",color="species",title ='종류 별 꽃받침 길이')
    st.plotly_chart(fig)
with col_1[1]:
    fig = px.box(df, x="species", y="sepal_width",color="species",title ='종류 별 꽃받침 너비')
    st.plotly_chart(fig)
    
col_2 = st.columns(2)
with col_2[0]:
    fig = px.box(df, x="species", y="petal_length",color="species",title='종류 별 꽃잎 길이')
    st.plotly_chart(fig)
with col_2[1]:
    fig = px.box(df, x="species", y="petal_width",color="species",title='종류 별 꽃잎 너비')
    st.plotly_chart(fig)
    
####    Hist and Curve Plot   ####

group_labels = ['setosa','versicolor','virginica']
colors = ['#393E46', '#2BCDC1', '#F66095']

col_sp_len = st.columns(2)
with col_sp_len[0]:
    x1_sp_len = df[df['species'] == 'setosa']['sepal_length'].tolist()
    x2_sp_len = df[df['species'] == 'versicolor']['sepal_length'].tolist()
    x3_sp_len = df[df['species'] == 'virginica']['sepal_length'].tolist()
    hist_df_sp_len = [x1_sp_len, x2_sp_len, x3_sp_len]
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_df_sp_len , group_labels, colors=colors,show_rug=False)
    # Add title
    fig.update_layout(title_text='종류 별 꽃받침 길이 Hist and Curve Plot')
    st.plotly_chart(fig)

with col_sp_len[1]:
    x1_sp_wid = df[df['species'] == 'setosa']['sepal_width'].tolist()
    x2_sp_wid = df[df['species'] == 'versicolor']['sepal_width'].tolist()
    x3_sp_wid = df[df['species'] == 'virginica']['sepal_width'].tolist()
    hist_df_sp_wid = [x1_sp_wid, x2_sp_wid, x3_sp_wid]
    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_df_sp_wid , group_labels, colors=colors,show_rug=False)
    # Add title
    fig.update_layout(title_text='종류 별 꽃받침 너비 Hist and Curve Plot')
    st.plotly_chart(fig)

col_pt = st.columns(2)
with col_pt[0]:
    # Petal Length
    x1_pt_len = df[df['species'] == 'setosa']['petal_length'].tolist()
    x2_pt_len = df[df['species'] == 'versicolor']['petal_length'].tolist()
    x3_pt_len = df[df['species'] == 'virginica']['petal_length'].tolist()
    hist_df_pt_len = [x1_pt_len, x2_pt_len, x3_pt_len]

    fig = ff.create_distplot(hist_df_pt_len, group_labels, colors=colors, show_rug=False)
    fig.update_layout(title_text='종류 별 꽃잎 길이 Hist and Curve Plot')
    st.plotly_chart(fig)

with col_pt[1]:
    # Petal Width
    x1_pt_wid = df[df['species'] == 'setosa']['petal_width'].tolist()
    x2_pt_wid = df[df['species'] == 'versicolor']['petal_width'].tolist()
    x3_pt_wid = df[df['species'] == 'virginica']['petal_width'].tolist()
    hist_df_pt_wid = [x1_pt_wid, x2_pt_wid, x3_pt_wid]

    fig = ff.create_distplot(hist_df_pt_wid, group_labels, colors=colors, show_rug=False)
    fig.update_layout(title_text='종류 별 꽃잎 너비 Hist and Curve Plot')
    st.plotly_chart(fig)
