import os
import time
import sounddevice as sd
import numpy as np
import queue
from openwakeword.model import Model
from faster_whisper import WhisperModel
import ollama

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
THRESHOLD = 0.5
COMMAND_DURATION = 5
DEVICE_ID = 1  # Headset Microphone (IER-EX15C)

print("Đang tải mô hình Wake word...")
model_path = os.path.abspath(os.path.join("models", "openwakeword", "hey_jarvis_v0.1.onnx"))
model_wakeword = Model(wakeword_models=[model_path], inference_framework="onnx")

print("Đang tải mô hình Whisper STT...")
model_whisper = WhisperModel("base", device="cpu", compute_type="int8")

audio_queue = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

print("\n=== HỆ THỐNG ĐÃ SẴN SÀNG ===")
print("Hãy nói 'Hey Jarvis' để đánh thức AI...\n")

try:
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                        blocksize=CHUNK_SIZE, dtype="int16",
                        device=DEVICE_ID,
                        callback=audio_callback):
        while True:
            chunk = audio_queue.get().flatten()
            prediction = model_wakeword.predict(chunk)
            score = prediction.get("hey_jarvis_v0.1", 0.0)

            if score > THRESHOLD:
                print(f"\n[JARVIS] Vâng, tôi nghe đây! (Điểm Wake word: {score:.2f})")

                # ---- QUAN TRỌNG: reset & dọn queue NGAY, trước khi làm gì khác ----
                model_wakeword.reset()
                with audio_queue.mutex:
                    audio_queue.queue.clear()

                print(f"[JARVIS] Đang thu âm câu lệnh trong {COMMAND_DURATION} giây...")
                command_audio = sd.rec(int(COMMAND_DURATION * SAMPLE_RATE),
                                       samplerate=SAMPLE_RATE, channels=1,
                                       dtype="float32", device=DEVICE_ID)
                sd.wait()

                print("[JARVIS] Đang dịch giọng nói thành văn bản...")
                command_audio_1d = command_audio.flatten()
                segments, info = model_whisper.transcribe(command_audio_1d, language="vi")

                user_text = "".join(segment.text for segment in segments).strip()
                print(f"\n-> BẠN NÓI: '{user_text}'")

                # response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': user_text}])

                print("\n--- Đang quay lại chế độ ngủ chờ 'Hey Jarvis' ---")

                # Dọn queue lần nữa để loại bỏ tiếng dội lại từ quá trình thu âm command
                with audio_queue.mutex:
                    audio_queue.queue.clear()

except KeyboardInterrupt:
    print("\n[HỆ THỐNG] Đã tắt trợ lý ảo thành công.")