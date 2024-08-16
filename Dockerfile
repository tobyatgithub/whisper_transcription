# Use the bitnami/pytorch image as the base
FROM bitnami/pytorch:latest

# Switch to root user to perform system updates and installations
USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir \
    transformers==4.33.3 \
    datasets==2.14.6 \
    librosa==0.10.1 \
    soundfile==0.12.1 \
    pydub==0.25.1 \
    openai-whisper==20231117 \
    pynvml==11.5.0

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY transcribe.py .

# Switch back to the non-root user
USER 1001

# Command to run when the container starts
CMD ["python", "transcribe.py"]