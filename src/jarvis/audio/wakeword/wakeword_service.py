# src/jarvis/audio/wakeword/wakeword_service.py
from openwakeword.model import Model

class WakewordService:
    def __init__(self, model_path):
        self.model = Model(wakeword_models=[model_path], inference_framework="onnx")

    def predict(self, chunk):
        prediction = self.model.predict(chunk)
        return prediction.get("hey_jarvis_v0.1", 0.0)

    def reset(self):
        self.model.reset()