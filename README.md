# **Intelligent Video Translation**

## **Project Overview**
The **Intelligent Video Translation** project translates audio from videos in one language into another, clones the original speaker’s voice, and overlays the translated audio back onto the video. The goal is to produce a translated video while retaining the original speaker’s voice characteristics.

## **Features**
- Extracts audio from videos.
- Transcribes audio into text.
- Translates the transcribed text into the target language.
- Generates speech from the translated text using voice cloning.
- Overlays the translated and cloned voice back onto the original video.

## **Project Structure**
```bash
.
├── extract_the_audio.py       # Script to extract audio from video
├── audio_to_text.py           # Script to transcribe audio from video
├── translate_text.py          # Script to translate transcribed text
├── text_to_audio.py           # Script to convert translated text to speech
├── combine_audio_video.py     # Script to combine the translated audio back to the video
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation (this file)
```

## Setup Instructions

### Prerequisites
- Python 3.11 or later (Ensure it is installed and added to your system's PATH).
- pip (Python's package installer).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhavan-P/Intelligent-Video-Translation.git
   cd Intelligent-Video-Translation

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Required Tools/Libraries
- MoviePy: For video and audio processing.
- Whisper: For transcription.
- DeepL API or Google Translate API: For translation.

### Running the Project
#### Step 1: Extract Audio from Video
Use the script to extract audio and transcribe it to text:
```bash
python audio_to_text.py --input_video path_to_video.mp4
```
This will create a transcription of the video's audio.

#### Step 2: Translate the Transcribed Text
Run the translation script to translate the extracted text into the target language:
```bash
python translate_text.py --input_text transcription.txt --source_lang en --target_lang ta
```

#### Step 3: Generate Speech from Translated Text
Convert the translated text into speech that mimics the original speaker's voice:
```bash
python text_to_speech.py --input_text translated_text.txt --original_audio path_to_original_speaker_audio.wav
```

#### Step 4: Combine Translated Audio with Original Video
Overlay the translated and cloned voice onto the original video:
```bash
python combine_audio_video.py --input_video path_to_video.mp4 --input_audio translated_speech.wav
```
This will produce the final video with the translated voice overlaid.

### Dependencies
The project requires the following Python libraries and tools:

- moviepy
- whisper
- torch
- transformers
- googletrans (or DeepL API, depending on your choice of translation service)
- soundfile
- numpy

These can be installed via the requirements.txt file.
