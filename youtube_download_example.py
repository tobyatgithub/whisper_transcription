import yt_dlp

def download_audio(youtube_url, output_path='audio.mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=Cv74Dv1Y4_g'
download_audio(youtube_url, 'output_audio')