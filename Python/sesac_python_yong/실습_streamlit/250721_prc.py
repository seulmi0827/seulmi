import streamlit as st
import pymysql
from pymysql.cursors import DictCursor 
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer,String, MetaData
import pandas as pd
from faker import Faker
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px


engine = create_engine('sqlite:///stocks.db')
MetaData = MetaData()

def load_data():
    with engine.connect() as conn:
        query = 'SELECT * FROM stocks order by id desc limit 10;'
        return pd.read_sql(query,conn)
    
st_autorefresh(interval=1000)   

df = load_data()

st.title("Real-Time Stock Dashboard")

cols = st.columns(3)
with cols[0]:
    st.metric('Latest Price', f'${round(df.iloc[-1]["price"],2)}')

with cols[1]:
    st.metric('Latest Volume', df.iloc[-1]['volume'])

with cols[2]:
    price_change = round(df.iloc[-1]["price"] - df.iloc[-2]["price"],2)
    volume_change = int(round(df.iloc[-1]["volume"] - df.iloc[-2]["volume"],2))
    st.metric('Price Change', f'${price_change}', price_change)
    st.metric('Volume Change', f'{volume_change}', volume_change)


# Initialize figure

fig = make_subplots(rows=2, cols = 1,
                    row_heights=[0.7, 0.3], 
                    vertical_spacing=0.1, 
                    )

# Add Traces
fig.add_trace(
    go.Scatter(x=list(df['timestamp']),
               y=list(df['price']),
               name="price",
               line=dict(color="#007fff"),
               #mode='markers',
               showlegend=True,
               ),
    row=1, col = 1)
fig.add_trace(
    go.Bar(x=list(df['timestamp']),
               y=list(df['volume']),
               name="price",
                marker=dict(color="#ffdb58"),
               #mode='bar',
               showlegend=True,
               ),
    row = 2, col = 1)



fig.update_layout(title_text='Stock Price and Volume')
st.plotly_chart(fig)