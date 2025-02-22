from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
import os
from pathlib import Path
from utils import process_audio_file
from openvoice_model import OpenVoiceModel

app = FastAPI()

# Geçici dosyaların saklanacağı klasörü oluştur
UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# OpenVoice modelini başlat
model = OpenVoiceModel()

@app.post("/upload-audio")
async def upload_audio(audio_file: UploadFile = File(...)):
    """Ses dosyasını yükle ve işle"""
    try:
        # Dosya uzantısını kontrol et
        if not audio_file.filename.endswith(('.wav', '.mp3')):
            raise HTTPException(status_code=400, detail="Sadece .wav veya .mp3 dosyaları kabul edilir")
        
        # Dosyayı kaydet
        file_path = UPLOAD_DIR / audio_file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(audio_file.file, buffer)
        
        # Ses dosyasını işle
        processed_path = process_audio_file(file_path)
        
        return {"message": "Ses dosyası başarıyla yüklendi", "file_path": str(processed_path)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-voice")
async def generate_voice(text: str):
    """Verilen metni klonlanmış ses ile sentezle"""
    try:
        # Son yüklenen ses dosyasını bul
        input_files = list(UPLOAD_DIR.glob("*_processed.wav"))
        if not input_files:
            raise HTTPException(status_code=400, detail="Önce bir ses dosyası yüklemelisiniz")
        
        input_file = input_files[-1]
        
        # Sesi oluştur
        output_path = OUTPUT_DIR / f"generated_{text[:20]}.wav"
        model.generate_speech(input_file, text, output_path)
        
        return FileResponse(output_path)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 