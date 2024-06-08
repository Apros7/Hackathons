import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.io import wavfile
from scipy.signal import spectrogram
import os

st.title("Audio Spectrogram Viewer")

# Upload .wav file
uploaded_file = st.file_uploader("Upload a .wav file", type=["wav"])

# Temporary directory to save uploaded file
temp_dir = "temp_wav"
os.makedirs(temp_dir, exist_ok=True)

if uploaded_file is not None:
    file_path = os.path.join(temp_dir, uploaded_file.name)
    
    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Read the audio file
    rate, data = wavfile.read(file_path)
    
    # Display the audio player
    st.audio(uploaded_file, format='audio/wav')

    # Generate and display the spectrogram
    f, t, Sxx = spectrogram(data, rate)
    plt.figure(figsize=(10, 4))
    sns.heatmap(np.log(Sxx + 1e-10), cmap='viridis', xticklabels=False, yticklabels=False)
    plt.title("Spectrogram")
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    st.pyplot(plt)
