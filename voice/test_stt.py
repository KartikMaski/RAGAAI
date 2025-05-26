import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from voice.stt import transcribe_audio


print(transcribe_audio("audio.wav"))
