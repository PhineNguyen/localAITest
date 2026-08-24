# src/jarvis/audio/stt/stt_service.py
from faster_whisper import WhisperModel

class STTService:
    def __init__(self, model_name="small", device="cpu", compute_type="int8"):
        self.model = WhisperModel(model_name, device=device, compute_type=compute_type)

    def transcribe(self, audio_float32):
        segments, info = self.model.transcribe(audio_float32, language="en")
        return "".join(segment.text for segment in segments).strip()