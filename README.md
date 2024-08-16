# whisper_transcription

In this project, we try to use Whisper to conduct basic audio-to-text service.

## Introduction
Tech stack: pytorch + whisper + nvidia docker

## How to run
1. Get a sample audio file and add it to the current directory

2. Build docker image
```bash
docker build -t whisper-transcription .
```

3. Run the docker with audio mount
```bash
# docker run --gpus all -v %cd%:/app/audio whisper-transcription python transcribe.py /app/audio/s11.Pronunounce_workshop__11_.wmv
docker run --gpus all -v %cd%:/app/audio whisper-transcription python transcribe.py /app/audio
```

## More features
1. Fine-tuning and Optimization:

Experiment with different Whisper model sizes (tiny, base, small, medium, large) to find the best balance between speed and accuracy for your needs.
If you're working with specific types of audio (e.g., domain-specific terminology), you might want to explore fine-tuning the model on your data.


2. Batch Processing:

Modify the script to handle multiple audio files in a directory, which could be useful for processing large numbers of files.


3. Error Handling and Logging:

Implement more robust error handling and add logging to make troubleshooting easier in the future.


4. Performance Monitoring:

Add timing and resource usage monitoring to understand how long transcriptions take and how much GPU memory they use.


5. Web Interface:

Create a simple web interface for uploading audio files and displaying transcriptions, making it more user-friendly.


6. Output Formats:

Add options to save transcriptions in different formats (e.g., plain text, SRT for subtitles, JSON with timestamps).


7. Post-processing:

Implement post-processing steps like punctuation correction, speaker diarization, or formatting improvements.