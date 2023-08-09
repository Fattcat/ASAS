import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
from datetime import datetime

def record_audio(duration, output_folder):
    # Nahratie zvukovej nahrávky
    sample_rate = 44100  # Vzorkovacia frekvencia (Hz)
    print("Začiatok nahrávania...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
    sd.wait()  # Čakanie na dokončenie nahrávania

    # Získanie aktuálneho dátumu a času
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")

    # Vytvorenie názvu súboru s aktuálnym dátumom a časom
    filename = f"{timestamp}.wav"

    # Vytvorenie cesty k výstupnému súboru na USB kľúči
    output_path = os.path.join(output_folder, filename)

    # Uloženie nahrávky do .wav súboru na USB kľúči
    wav.write(output_path, sample_rate, recording)

    print(f"Nahrávka uložená v súbore '{output_path}'.")

def record_audio_continuous(duration, output_folder, interval):
    while True:
        record_audio(duration, output_folder)
        time.sleep(interval)

if __name__ == "__main__":
    duration_seconds = 8
    interval_seconds = 2
    usb_drive_letter = "E:/AllCaptured/CpMic/"

    output_folder_path = os.path.join(usb_drive_letter)

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    record_audio_continuous(duration_seconds, output_folder_path, interval_seconds)
