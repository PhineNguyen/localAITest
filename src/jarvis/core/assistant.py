# src/jarvis/core/assistant.py
import queue
from types import SimpleNamespace

import numpy as np
import sounddevice as sd


class JarvisAssistant:
    def __init__(self, wakeword_service, stt_service, tts_service, llm_client, settings):
        self.wakeword = wakeword_service
        self.stt = stt_service
        self.tts = tts_service
        self.llm = llm_client
        self.settings = self._normalize_settings(settings)
        self.audio_queue = queue.Queue()

    @staticmethod
    def _normalize_settings(settings):
        if hasattr(settings, "SAMPLE_RATE"):
            return settings
        if isinstance(settings, dict):
            return SimpleNamespace(**settings)
        raise TypeError("settings must be a module-like object or dict")

    def audio_callback(self, indata, frames, time_info, status):
        if status:
            print(status)
        self.audio_queue.put(indata.copy())

    def _get_audio_chunk(self, timeout=0.15):
        try:
            chunk = self.audio_queue.get(timeout=timeout)
            return chunk.flatten()
        except queue.Empty:
            return None

    def _get_input_device(self):
        devices = sd.query_devices()

        # Prefer the built-in MacBook microphone.
        # AirPods can then connect/disconnect without killing Jarvis input.
        for i, device in enumerate(devices):
            if (
                "MacBook Air Microphone" in device["name"]
                and device["max_input_channels"] > 0
            ):
                print(f"🎤 Input device: {device['name']}")
                return i

        print("🎤 MacBook microphone not found. Using system default input.")
        return None

    def run(self):
        with sd.InputStream(
            samplerate=self.settings.SAMPLE_RATE,
            channels=1,
            blocksize=self.settings.CHUNK_SIZE,
            dtype="int16",
            device=self._get_input_device(),
            callback=self.audio_callback
        ):
            while True:
                chunk = self._get_audio_chunk(timeout=0.2)
                if chunk is None:
                    continue

                score = self.wakeword.predict(chunk)

                if score > self.settings.THRESHOLD:
                    self.tts.speak("Yes, how can I help you?")
                    self.wakeword.reset()
                    self._clear_queue()

                    while True:
                        frames = []
                        num_chunks = int(self.settings.COMMAND_DURATION * self.settings.SAMPLE_RATE / self.settings.CHUNK_SIZE)

                        for _ in range(num_chunks):
                            chunk = self._get_audio_chunk(timeout=0.5)
                            if chunk is None:
                                self._clear_queue()
                                break
                            frames.append(chunk)

                        if not frames:
                            break

                        command_audio = np.concatenate(frames, axis=0).flatten()
                        audio_float = command_audio.astype(np.float32) / 32768.0
                        user_text = self.stt.transcribe(audio_float)

                        if not user_text:
                            self._clear_queue()
                            continue

                        if "bye" in user_text.lower():
                            self.tts.speak("See you later! Take care.")
                            break

                        reply = self.llm.chat(user_text)
                        self.tts.speak(reply)
                        self._clear_queue()

    def _clear_queue(self):
        with self.audio_queue.mutex:
            self.audio_queue.queue.clear()