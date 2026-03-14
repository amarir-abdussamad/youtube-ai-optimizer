import yt_dlp
import whisper

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',      # grab best audio stream available
        'outtmpl': 'audio.%(ext)s',      # output filename: audio.mp3, audio.webm, etc.
        'postprocessors': [{             # postprocessors run AFTER download
            'key': 'FFmpegExtractAudio', # use ffmpeg to extract audio
            'preferredcodec': 'mp3',     # convert to mp3   
        }],
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio downloaded successfully!")
        return "audio.mp3"

    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None
    

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    audio_path = download_audio(url)         # Step 1: download
    if audio_path:
        transcript = transcribe_audio(audio_path) # Step 2: transcribe
        print(transcript)
