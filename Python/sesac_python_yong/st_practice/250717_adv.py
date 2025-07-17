import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

# Load dataset
df = px.data.iris()

# Initialize figure
fig = go.Figure()

# Add Traces

fig.add_trace(
    go.Scatter(x=list(df[df['species']=='setosa'].sepal_length),
               y=list(df[df['species']=='setosa'].sepal_width),
               name="setosa",
               line=dict(color="DarkBlue"),
               mode='markers',
               showlegend=True),)

fig.add_trace(
    go.Scatter(x=list(df[df['species']=='virginica'].sepal_length),
               y=list(df[df['species']=='virginica'].sepal_width),
               name="virginica",
               line=dict(color="Green"),
               mode='markers',
               showlegend=True))

fig.add_trace(
    go.Scatter(x=list(df[df['species']=='versicolor'].sepal_length),
               y=list(df[df['species']=='versicolor'].sepal_width),
               name="versicolor",
               line=dict(color="Crimson"),
               mode='markers',
               showlegend=True))


fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {"title": "All",
                            #"annotations": []
                            }]),
                dict(label="setosa",
                     method="update",
                     args=[{"visible": [True, False, False]},
                           {"title": "setosa",
                            #"annotations": setosa_annotations
                            }])
                            ,
                dict(label="virginica",
                     method="update",
                     args=[{"visible": [False, True, False]},
                           {"title": "virginica",
                            #"annotations": low_annotations
                            }]),
                dict(label="versicolor",
                     method="update",
                     args=[{"visible": [False, False,True]},
                           {"title": "versicolor",
                            #"annotations": high_annotations + low_annotations
                            }]),
            ]),
        )
    ])

# Set title
fig.update_layout(title_text="Iris")

st.plotly_chart(fig)
