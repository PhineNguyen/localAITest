# test_wakeword.py
from src.jarvis.config import settings
from src.jarvis.audio.wakeword.wakeword_service import WakewordService
from src.jarvis.audio.stt.stt_service import STTService
from src.jarvis.audio.tts.tts_service import TTSService
from src.jarvis.llm.ollama_client import OllamaClient
from src.jarvis.core.assistant import JarvisAssistant



wakeword = WakewordService(settings.WAKEWORD_MODEL_PATH)
stt = STTService("small", "cpu", "int8")
tts = TTSService(settings.PIPER_MODEL_PATH)
llm = OllamaClient(settings.OLLAMA_MODEL)
assistant = JarvisAssistant(wakeword, stt, tts, llm, settings)
assistant.run()   