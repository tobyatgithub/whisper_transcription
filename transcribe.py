import sys
import os
import whisper
from pydub import AudioSegment
import time
import pynvml

def initialize_gpu():
    pynvml.nvmlInit()
    return pynvml.nvmlDeviceGetHandleByIndex(0)

def get_gpu_memory_usage(handle):
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    return info.used / 1024 / 1024  # Convert to MB

def transcribe_audio(file_path, handle):
    # Load the Whisper model
    # Choose from (tiny, base, small, medium, large) 
    start_time = time.time()
    model = whisper.load_model("base")
    load_time = time.time() - start_time
    load_memory = get_gpu_memory_usage(handle)

    # Load the audio file
    audio = whisper.load_audio(file_path)

    # Transcribe the audio
    start_time = time.time()
    result = model.transcribe(audio)
    transcribe_time = time.time() - start_time
    transcribe_memory = get_gpu_memory_usage(handle)

    return result["text"], load_time, transcribe_time, load_memory, transcribe_memory

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

    handle = initialize_gpu()
    
    try:
        transcription, load_time, transcribe_time, load_memory, transcribe_memory = transcribe_audio(audio_file, handle)
        output_file = os.path.splitext(audio_file)[0] + '.txt'
        with open(output_file, 'w') as f:
            f.write(transcription)
        print("Transcription:")
        print(transcription)
        print("\nPerformance metrics:")
        print(f"  Model load time: {load_time:.2f} seconds")
        print(f"  Transcription time: {transcribe_time:.2f} seconds")
        print(f"  GPU memory usage during model load: {load_memory:.2f} MB")
        print(f"  GPU memory usage during transcription: {transcribe_memory:.2f} MB")
    except Exception as e:
        print(f"Error processing {audio_file}: {str(e)}")
    finally:
        pynvml.nvmlShutdown()