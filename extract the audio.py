from moviepy.editor import VideoFileClip

# Load the video file
video = VideoFileClip("inputvideo.mp4")

# Extract the audio
audio = video.audio

# Save the extracted audio
audio.write_audiofile("extracted_audio.wav")
