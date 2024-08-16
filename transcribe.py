import sys
import whisper
from pydub import AudioSegment

def transcribe_audio(file_path):
    # Load the Whisper model
    # Choose from (tiny, base, small, medium, large) 
    model = whisper.load_model("base")

    # Load the audio file
    audio = whisper.load_audio(file_path)

    # Transcribe the audio
    result = model.transcribe(audio)

    return result["text"]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <path_to_audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    
    # Convert mp3 to wav if necessary
    if audio_file.endswith('.mp3'):
        wav_file = audio_file.rsplit('.', 1)[0] + '.wav'
        audio = AudioSegment.from_mp3(audio_file)
        audio.export(wav_file, format="wav")
        audio_file = wav_file

    transcription = transcribe_audio(audio_file)
    print("Transcription:")
    print(transcription)