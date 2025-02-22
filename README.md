# VoiceClone
# XTTS v2 ile Ses Klonlama Projesi (XTTS v2)

Bu proje, XTTS v2 (OpenVoice) kullanarak ses klonlama ve metin-ses dönüşümü yapmanızı sağlar.

## Kurulum Adımları

1. Python Sanal Ortam Oluşturma (önerilen):

⌘K to generate a command
Bir Python projesi oluştur. Bu proje, kullanıcıdan bir ses dosyası alıp XTTS v2 (OpenVoice) kullanarak sesi klonlayıp yeni bir metinle sentezlenmiş ses üretmelidir.  
Projede aşağıdaki yapıları oluştur:  

1. `app.py`: FastAPI ile bir backend oluştur.  
   - `/upload-audio`: Kullanıcının ses dosyasını yüklemesi için bir endpoint oluştur.  
   - `/generate-voice`: Kullanıcının istediği metni girmesiyle klonlanmış ses üretmesi için bir endpoint oluştur.  

2. `requirements.txt`: Gerekli kütüphaneleri ekle:
   - `fastapi`
   - `uvicorn`
   - `torch`
   - `transformers`
   - `numpy`
   - `scipy`
   - `pydub`
   - `openvoice` (XTTS v2 için)
   - `ffmpeg-python` (ses işleme için)

3. `utils.py`: Ses dosyası işleme fonksiyonları yaz:
   - Ses dosyasını doğru formata çeviren bir fonksiyon.
   - OpenVoice modeline uygun hale getiren bir fonksiyon.

4. `openvoice_model.py`: XTTS v2 modelini yükleyip çalıştıran kodu yaz.


Size XTTS v2 kullanarak ses klonlama projesi için gerekli dosyaları oluşturacağım. Her dosyayı sırayla açıklayarak paylaşacağım.
İlk olarak requirements.txt dosyası ile başlayalım:
0
Şimdi ana uygulama dosyası olan app.py'yi oluşturalım:

Şimdi ses işleme yardımcı fonksiyonlarını içeren utils.py dosyasını oluşturalım:
normalized
XTTS modelini yöneten openvoice_model.py dosyasını oluşturalım:

Son olarak, README.md dosyasını oluşturalım:
:
bash
pip install -r requirements.txt
:
bash
uvicorn app:app --reload
:
bash
curl -X POST -F "audio_file=@referans.wav" http://localhost:8000/upload-audio
:
bash
curl -X POST -d "text=Merhaba Dünya" http://localhost:8000/generate-voice --output output.wav
dönüştürülür
Bu proje yapısı ile:
Ses dosyalarını yükleyebilir
Yüklenen sesi XTTS v2 modeli için uygun formata dönüştürebilir
3. Yeni metinler için klonlanmış ses üretebilirsiniz
Projeyi çalıştırmak için önce gereksinimleri yükleyin ve ardından FastAPI sunucusunu başlatın. Tüm işlemler yerel olarak gerçekleştirilir ve herhangi bir veritabanı gerektirmez.
Projeyi nasıl ayağa kaldıracağım

Size projeyi nasıl ayağa kaldıracağınızı adım adım açıklayacağım. Öncelikle README.md dosyasını güncelleyelim:
:
bash
python -m venv venv
:
bash
.\venv\Scripts\activate
:
bash
source venv/bin/activate
:
bash
pip install -r requirements.txt
:
bash
mkdir uploads outputs
:
bash
python -m uvicorn app:app --reload
:
bash
curl -X POST -F "audio_file=@/path/to/your/audio.wav" http://localhost:8000/upload-audio
:
bash
curl -X POST "http://localhost:8000/generate-voice?text=Merhaba Dünya" --output output.wav
:
bash
pip install uvicorn
:
bash
ffmpeg -version
olun
Projeyi çalıştırmak için adım adım yapmanız gerekenler:
İlk olarak, projenin ana dizininde bir terminal açın
Python sanal ortam oluşturun ve aktifleştirin:
için
Gerekli paketleri yükleyin:
txt
Gerekli klasörleri oluşturun:
outputs
Sunucuyu başlatın:
reload
Sunucu başladıktan sonra:
API dokümantasyonu: http://localhost:8000/docs
Ses yükleme endpoint'i: http://localhost:8000/upload-audio
Ses üretme endpoint'i: http://localhost:8000/generate-voice
Eğer "command not found: uvicorn" hatası alıyorsanız, bu sanal ortamın aktif olmadığı veya uvicorn'un doğru yüklenmediği anlamına gelir. Bu durumda yukarıdaki adımları tekrar takip edin.
bunları readme.md dosyasına yaz

Tabii, README.md dosyasını güncelleyeceğim:
# Ses Klonlama Projesi (XTTS v2)

Bu proje, XTTS v2 (OpenVoice) kullanarak ses klonlama ve metin-ses dönüşümü yapmanızı sağlar.

## Kurulum Adımları

1. Python Sanal Ortam Oluşturma (önerilen):
bash
python -m venv venv
```

2. Sanal Ortamı Aktifleştirme:

```bash
source venv/bin/activate # Linux/Mac için
```

3. Gerekli Paketlerin Yüklenmesi:

```bash
pip install -r requirements.txt
```

4. FFmpeg Kurulumu:
- Windows: `choco install ffmpeg`
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

## Projeyi Çalıştırma

1. Gerekli klasörlerin oluşturulduğundan emin olun:
bash
mkdir uploads outputs

2. FastAPI Sunucusunu Başlatma:
python -m uvicorn app:app --reload

3. Tarayıcıda API dokümantasyonuna erişim:
- http://localhost:8000/docs

## API Kullanımı

1. Ses Dosyası Yükleme:
bash
curl -X POST -F "audio_file=@/path/to/your/audio.wav" http://localhost:8000/upload-audio

2. Ses Üretme:
bash
curl -X POST "http://localhost:8000/generate-voice?text=Merhaba Dünya" --output output.wav


## Notlar

- Desteklenen ses formatları: .wav ve .mp3
- Yüklenen ses dosyaları `uploads` klasöründe saklanır
- Üretilen sesler `outputs` klasöründe saklanır
- Model ilk başlatıldığında gerekli dosyaları indirecektir
- GPU varsa otomatik olarak kullanılacaktır

## Hata Giderme

1. "command not found: uvicorn" hatası alırsanız:
bash
pip install uvicorn

2. FFmpeg hatası alırsanız, FFmpeg'in doğru kurulduğundan emin olun:
bash
ffmpeg -version

3. Ses dosyası yüklenirken hata alırsanız:
bash
curl -X POST -F "audio_file=@/path/to/your/audio.wav" http://localhost:8000/upload-audio