import os
import time
import sounddevice as sd
import numpy as np
import queue
from openwakeword.model import Model
from faster_whisper import WhisperModel
import ollama
from piper import PiperVoice
import wave
import io

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280
THRESHOLD = 0.5
COMMAND_DURATION = 5
DEVICE_ID = 1  

print("Đang tải mô hình Wake word...")
model_path = os.path.abspath(os.path.join("models", "openwakeword", "hey_jarvis_v0.1.onnx"))
model_wakeword = Model(wakeword_models=[model_path], inference_framework="onnx")

print("Đang tải mô hình Whisper STT...")
model_whisper = WhisperModel("small", device="cpu", compute_type="int8")

print("Đang tải mô hình Piper TTS...")
voice_model_path = os.path.abspath(os.path.join("models", "piper", "en_US-lessac-medium.onnx"))
piper_voice = PiperVoice.load(voice_model_path)

def speak(text):
    audio_stream = io.BytesIO()
    with wave.open(audio_stream, "wb") as wav_file:
        piper_voice.synthesize_wav(text, wav_file)
    
    audio_stream.seek(0)
    with wave.open(audio_stream, "rb") as wav_file:
        audio_data = wav_file.readframes(wav_file.getnframes())
        audio_np = np.frombuffer(audio_data, dtype=np.int16)
        sample_rate = wav_file.getframerate()
    
    sd.play(audio_np, samplerate=sample_rate)
    sd.wait()  # chờ phát xong mới chạy tiếp
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
                speak("Yes, how can I help you?")

                # ---- QUAN TRỌNG: reset & dọn queue NGAY, trước khi làm gì khác ----
                model_wakeword.reset()
                with audio_queue.mutex:
                    audio_queue.queue.clear()

                conversation_active = True
                while conversation_active:
                    # Thu âm bằng cách lấy chunk từ cùng 1 stream, KHÔNG mở stream mới
                    num_chunks = int(COMMAND_DURATION * SAMPLE_RATE / CHUNK_SIZE)
                    frames = []
                    for _ in range(num_chunks):
                        chunk = audio_queue.get()
                        frames.append(chunk)
        
                    command_audio = np.concatenate(frames, axis=0).flatten()
                    # Chuyển từ int16 sang float32 vì Whisper cần float32 chuẩn hóa -1.0 đến 1.0
                    command_audio_1d = command_audio.astype(np.float32) / 32768.0
                    segments, info = model_whisper.transcribe(command_audio_1d, language="en")

                    user_text = "".join(segment.text for segment in segments).strip()
                    
                    print(f"\n-> BẠN NÓI: '{user_text}'")

                    if not user_text:
                        with audio_queue.mutex:
                            audio_queue.queue.clear()
                        continue  # Nếu không có văn bản, tiếp tục lắng nghe
                
                    if "bye" in user_text.lower():
                        speak("See you later! Take care.")
                        break
                    response = ollama.chat(
                        model="llama3.1:8b", 
                        messages=[{"role": "system", "content": "You are a voice assistant named Jarvis. Respond briefly and naturally, as if you were having a conversation, but provide enough detail to be helpful. Avoid lengthy lists."},
                                {"role": "user", "content": user_text}
                            ],
                    options={"num_predict": 300}
                    )
                    ai_reply = response["message"]["content"]
                    speak(ai_reply)
                    print(f"\n[JARVIS] {ai_reply}")
                    # ---- DỌN QUEUE NGAY SAU KHI OLLAMA XONG, TRƯỚC KHI KIỂM TRA BYE ----
                    with audio_queue.mutex:
                        audio_queue.queue.clear()                  
                 
                

except KeyboardInterrupt:
    print("\n[HỆ THỐNG] Đã tắt trợ lý ảo thành công.")
    
