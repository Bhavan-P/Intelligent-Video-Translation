from gtts import gTTS

# Read the translated text from the file
with open("translated_text.txt", "r", encoding="utf-8") as file:
    translated_text = file.read()

# Convert the text to audio using gTTS
try:
    tts = gTTS(text=translated_text, lang='ta')  # 'ta' for Tamil
    tts.save("translated_audio.mp3")  # Save the audio file

    print("Audio successfully saved as 'translated_audio.mp3'!")
except Exception as e:
    print(f"Error during text-to-speech conversion: {e}")
