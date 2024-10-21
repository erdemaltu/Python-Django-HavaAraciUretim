# Resmi Python 3.11 imajını temel alın
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyalarını kopyala ve yükle
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Portu belirt
EXPOSE 8000

# Uygulama sunucusunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
