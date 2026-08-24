# src/jarvis/audio/tts/tts_service.py
import io
import wave
import numpy as np
import sounddevice as sd
from piper import PiperVoice


class TTSService:
    def __init__(self, model_path):
        self.voice = PiperVoice.load(model_path)

    def speak(self, text):
        audio_stream = io.BytesIO()
        with wave.open(audio_stream, "wb") as wav_file:
            self.voice.synthesize_wav(text, wav_file)

        audio_stream.seek(0)
        with wave.open(audio_stream, "rb") as wav_file:
            audio_data = wav_file.readframes(wav_file.getnframes())
            audio_np = np.frombuffer(audio_data, dtype=np.int16)
            sample_rate = wav_file.getframerate()

        sd.play(audio_np, samplerate=sample_rate)
        sd.wait()