import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



freq_input = st.slider('Frequency',1,10)

amp_input = st.slider('Amplitude',1,10)



x = np.linspace(0,10,100) * freq_input
y = np.sin(x) * amp_input

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title(f'Sine Wave: Frequency = {freq_input}, Amplitude = {amp_input}')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.legend()

st.pyplot(fig)

st.write('슬라이더를 사용하여 사인파의 주파수와 진폭을 조정할 수 있습니다.')