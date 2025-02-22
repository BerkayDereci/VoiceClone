import torch
from transformers import AutoProcessor, AutoModel
import numpy as np
from pathlib import Path

class OpenVoiceModel:
    def __init__(self):
        """XTTS v2 modelini yükle ve hazırla"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Model ve işlemciyi yükle
        self.processor = AutoProcessor.from_pretrained("openai/whisper-small")
        self.model = AutoModel.from_pretrained("openvoice/xtts-v2")
        self.model.to(self.device)
    
    def generate_speech(self, reference_audio: Path, text: str, output_path: Path):
        """Referans ses kullanarak yeni metin için ses üret"""
        
        # Referans sesi yükle ve işle
        audio_features = self.processor(reference_audio)
        
        # Metni işle
        text_inputs = self.processor(text, return_tensors="pt")
        
        # Sesi üret
        with torch.no_grad():
            generated_speech = self.model.generate(
                text_inputs.input_ids.to(self.device),
                audio_features=audio_features.to(self.device)
            )
        
        # Sesi kaydet
        self.save_audio(generated_speech.cpu().numpy(), output_path)
    
    @staticmethod
    def save_audio(audio_array: np.ndarray, output_path: Path):
        """Ses dizisini WAV dosyası olarak kaydet"""
        import scipy.io.wavfile as wav
        wav.write(output_path, 16000, audio_array) 