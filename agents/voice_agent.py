from transformers import pipeline
import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os
from gtts import gTTS

stt_model = whisper.load_model("base")

def transcribe_audio(file_path=None, duration=5):
    if file_path:
        result = stt_model.transcribe(file_path)
        return result["text"]

    print("🎙️ Recording...")
    fs = 44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("✅ Done recording.")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        wav.write(tmpfile.name, fs, recording)
        result = stt_model.transcribe(tmpfile.name)
        os.unlink(tmpfile.name)
        return result["text"]

def speak_text(text):
    tts = gTTS(text=text)
    tts.save("response.mp3")
    os.system("start response.mp3" if os.name == "nt" else "afplay response.mp3")
