from pydub import AudioSegment 
  
audio = AudioSegment.from_mp3("Data/240515 Subject 5.mp3") 

# Define the start and end times (in milliseconds)
start_time = 18 * 1000  # 26 seconds * 1000 = milliseconds
end_time = 30 * 1000  # 30 seconds * 1000 = milliseconds

# Extract the segment
extracted_segment = audio[start_time:end_time]

# Export the extracted segment
extracted_segment.export("output.mp3", format="mp3")

print("Audio cut and saved successfully.")