from pydub import AudioSegment
import numpy as np
from pathlib import Path
import ffmpeg

def process_audio_file(file_path: Path) -> Path:
    """Ses dosyasını işleyerek XTTS modeli için uygun formata çevirir"""
    
    # Ses dosyasını yükle
    audio = AudioSegment.from_file(file_path)
    
    # Ses özelliklerini düzenle
    audio = audio.set_channels(1)  # Mono
    audio = audio.set_frame_rate(16000)  # 16kHz örnekleme hızı
    
    # Processed dosya yolu
    processed_path = file_path.parent / f"{file_path.stem}_processed.wav"
    
    # WAV formatında kaydet
    audio.export(processed_path, format="wav")
    
    return processed_path

def normalize_audio(audio_path: Path) -> np.ndarray:
    """Ses dosyasını normalize eder"""
    audio = AudioSegment.from_wav(audio_path)
    samples = np.array(audio.get_array_of_samples())
    
    # Normalize
    normalized = samples / np.max(np.abs(samples))
    return normalized 