import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio to text
result = model.transcribe("extracted_audio.wav")
transcription = result['text']

# Save the transcription with UTF-8 encoding
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcription)

print("Transcription:", transcription)
