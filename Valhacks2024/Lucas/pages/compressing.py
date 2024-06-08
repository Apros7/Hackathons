import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Navigation

st.title("Compression")

# Top KPIs
col1, col2 = st.columns(2)
col1.metric("Time to compress 1 minute of audio (on macbook)", "~30 ms", "")
col2.metric("Size of model", "11 kb", "")

col3 = st.columns(1)[0]
col3.metric("Less data sent over cloud", "13x", "")

col3, col4 = st.columns(2)
col3.metric("Time to run 1 minute of detection", "1.2 sec", "")
col4.metric("Breathing variance detection", "Stable, slighty unstable & dangerous", "")

fig, ax = plt.subplots(1, 2, figsize=(16, 8))

labels_1 = ['Not able to detect', 'Correct detection', 'Not correct detection']
sizes_1 = [40, 48, 12]
ax[0].pie(sizes_1, labels=labels_1, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
ax[0].set_title('Accuracy')

labels_2 = ['Stable', 'Slighty unstable']
sizes_2 = [99.5, 0.5]
ax[1].pie(sizes_2, labels=labels_2, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
ax[1].set_title('Type of breathing variance')

st.pyplot(fig)
