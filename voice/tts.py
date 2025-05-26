from gtts import gTTS
import os

def speak_text(text: str, output_file="response.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    os.system(f"start {output_file}" if os.name == "nt" else f"xdg-open {output_file}")
