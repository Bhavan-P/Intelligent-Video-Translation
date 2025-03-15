import whisper
from googletrans import Translator

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio file to text
try:
    result = model.transcribe("extracted_audio.wav")
    
    # Check if transcription was successful
    if 'text' in result:
        transcription = result['text']
        print("Transcription:", transcription)

        # Save transcription to a file
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(transcription)
    else:
        print("Error: 'text' not found in result. Transcription might have failed.")
except Exception as e:
    print(f"Error during transcription: {e}")
    transcription = None

# Proceed with translation only if transcription was successful
if transcription:
    # Initialize translator
    translator = Translator()

    try:
        # Translate text from English to Tamil
        translated = translator.translate(transcription, src='en', dest='ta')
        translated_text = translated.text

        # Post-processing for better formatting
        translated_text = translated_text.replace(".", ". ").replace("?", "? ").replace("!", "! ")
        translated_text = ' '.join(translated_text.split())  # Remove extra spaces

        # More advanced cleaning for broken words can be done here (if necessary)
        # Example: you can implement a function to check for common errors.

        # Save the translated text to a file
        with open("translated_text.txt", "w", encoding="utf-8") as f:
            f.write(translated_text)

        print("Translated Text:", translated_text)

    except Exception as e:
        print(f"Error during translation: {e}")
else:
    print("Transcription was not successful, skipping translation.")

