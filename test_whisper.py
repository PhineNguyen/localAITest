import sounddevice as sd
import numpy as np
import wave
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5

print("Speak now...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()

print("Recording finished.")

with wave.open("recording.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio.tobytes())

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcribing...")

segments, info = model.transcribe(
    "recording.wav",
    language="vi"
)

print("Detected language:", info.language)

for segment in segments:
    print("Text:", segment.text)
