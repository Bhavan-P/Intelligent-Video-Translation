from moviepy.editor import VideoFileClip, AudioFileClip

# Load the original video
video = VideoFileClip("inputvideo.mp4")

# Load the generated translated audio
translated_audio = AudioFileClip("translated_audio.mp3")

# Set the translated audio as the new audio for the video
video_with_translated_audio = video.set_audio(translated_audio)

# Save the final video with the translated audio
video_with_translated_audio.write_videofile("final_video_with_translation.mp4", codec="libx264", audio_codec="aac")
