import streamlit as st
from transcribe import transcribe_audio

st.title("🎤 Whisper Speech-to-Text Transcriber")

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a", "ogg"])

if audio_file:
    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_file)
    st.subheader("Transcript")
    st.text_area("Text", transcript, height=300)
    st.download_button("Download Transcript", transcript, file_name="transcript.txt")