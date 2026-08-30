import os
import subprocess
import tempfile
import wave

from piper import PiperVoice


class TTSService:
    def __init__(self, model_path):
        self.voice = PiperVoice.load(model_path)

    def speak(self, text):
        temp_path = None

        try:
            # Create a temporary WAV file
            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as temp_file:
                temp_path = temp_file.name

            # Let Piper write the synthesized speech directly to WAV
            with wave.open(temp_path, "wb") as wav_file:
                self.voice.synthesize_wav(text, wav_file)

            # afplay follows the CURRENT macOS output device
            subprocess.run(
                ["afplay", temp_path],
                check=True
            )

        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)
