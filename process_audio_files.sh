#!/bin/bash

# # Run youtube_download_example.py first
# python youtube_download_example.py
# echo "youtube download finished."

# Process all audio files
for file in *.mp3 *.wav; do
    if [ -f "$file" ]; then
        echo "Processing $file"
        python transcribe.py "$file"
    fi
done

echo "All audio files have been processed."

