import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Multi-Page App", layout="wide")

# Navigation

st.title("Our approach")

st.image("Valhacks2024/Lucas/structure.png", caption="Cloud structure of our system approach", use_column_width=True)

# Top KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Metric 1", "1234", "4.5%")
col2.metric("Metric 2", "5678", "-2.3%")
col3.metric("Metric 3", "91011", "7.8%")

# Ring diagrams (Donut charts)
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

labels_1 = ['A', 'B', 'C']
sizes_1 = [20, 35, 45]
ax[0].pie(sizes_1, labels=labels_1, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
ax[0].set_title('Ring Diagram 1')

labels_2 = ['X', 'Y', 'Z']
sizes_2 = [25, 30, 45]
ax[1].pie(sizes_2, labels=labels_2, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
ax[1].set_title('Ring Diagram 2')

st.pyplot(fig)
