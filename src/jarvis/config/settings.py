# src/jarvis/config/settings.py
SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
THRESHOLD = 0.5
COMMAND_DURATION = 5
DEVICE_ID = 1
WAKEWORD_MODEL_PATH = "models/openwakeword/hey_jarvis_v0.1.onnx"
WHISPER_MODEL = "small"
PIPER_MODEL_PATH = "models/piper/en_US-lessac-medium.onnx"
OLLAMA_MODEL = "llama3.1:8b"