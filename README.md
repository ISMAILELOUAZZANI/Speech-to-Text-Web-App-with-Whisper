# Whisper Speech-to-Text Transcription Web App

A simple web app for transcribing audio files into text using OpenAI's Whisper model.

## Features

- Upload audio files (WAV, MP3, etc.)
- Transcribe speech to text
- Download the transcript
- Simple Streamlit UI

## Quick Start

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the app:
    ```
    streamlit run src/app.py
    ```

## Project Structure

- `src/` — source code
- `requirements.txt` — dependencies
- `README.md` — documentation

## License

MIT License

---

**Note:** To use GPU acceleration, make sure you have PyTorch with CUDA installed.