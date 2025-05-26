import streamlit as st
import requests
import tempfile
from pathlib import Path
from pydub import AudioSegment
import os

st.set_page_config(page_title="Finance Assistant", layout="centered")
st.title("📊 Voice Market Brief Assistant")

FASTAPI_BASE = "http://localhost:8000"

option = st.radio("Choose Input Method:", ["Text Query", "Voice Upload"])

if option == "Text Query":
    st.write("For now, use the predefined use case to get a market briefing.")
    if st.button("Get Market Brief"):
        with st.spinner("Generating market briefing..."):
            response = requests.get(f"{FASTAPI_BASE}/brief")
            if response.status_code == 200:
                data = response.json()
                st.subheader("📢 Summary:")
                st.success(data["summary"])
                st.subheader("📄 Context:")
                st.code(data["context_used"])

                if Path("response.mp3").exists():
                    st.audio("response.mp3", format="audio/mp3")
            else:
                st.error("Failed to get market brief.")

elif option == "Voice Upload":
    uploaded_file = st.file_uploader("Upload a voice file (WAV format preferred)", type=["wav", "mp3", "m4a"])

    if uploaded_file:
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            temp_file_path = tmp.name

        if st.button("Transcribe Voice"):
            with open(temp_file_path, "rb") as f:
                files = {"file": (uploaded_file.name, f, "audio/wav")}
                with st.spinner("Transcribing..."):
                    response = requests.post(f"{FASTAPI_BASE}/voice-query/", files=files)

            if response.status_code == 200:
                transcription = response.json()["transcription"]
                st.subheader("🗣️ Transcription:")
                st.info(transcription)
            else:
                st.error("Voice processing failed.")
