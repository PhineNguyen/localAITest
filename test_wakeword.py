import sounddevice as sd
import numpy as np
from openwakeword.model import Model

SAMPLE_RATE = 16000
DURATION = 5
CHUNK_SIZE = 1280

print("Loading wake word models...")

model = Model(inference_framework="onnx")

print("Say 'Hey Jarvis' within 5 seconds...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)

sd.wait()
audio = audio.flatten()

print("Running detection...")

max_scores = {}

for i in range(0, len(audio), CHUNK_SIZE):
    chunk = audio[i:i + CHUNK_SIZE]

    if len(chunk) < CHUNK_SIZE:
        break

    prediction = model.predict(chunk)

    for wakeword, score in prediction.items():
        if wakeword not in max_scores:
            max_scores[wakeword] = score
        else:
            max_scores[wakeword] = max(max_scores[wakeword], score)

for wakeword, score in max_scores.items():
    print(wakeword, ":", score)