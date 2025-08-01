import whisper
import tempfile
import os

def load_model():
    # Use "base" for speed or "small"/"medium"/"large" for accuracy
    return whisper.load_model("base")

def transcribe_audio(audio_file):
    model = load_model()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.read())
        tmp.flush()
        result = model.transcribe(tmp.name)
    os.unlink(tmp.name)
    return result["text"]