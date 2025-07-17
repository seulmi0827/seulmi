import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y, label = 'Sine Wave')
ax.set_title('Matplotlib Example')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.legend()

st.pyplot(fig)