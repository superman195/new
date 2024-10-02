import whisper

# Load the Whisper model
model = whisper.load_model("base")  # You can choose other models like "tiny", "small", "medium", or "large"

# Transcribe the MP4 file
result = model.transcribe("1.mp4")

# Print the transcription
print(result['text'])
