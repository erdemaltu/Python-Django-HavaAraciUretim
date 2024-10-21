
# Hava Aracı Üretim Uygulaması

Bu proje, bir hava aracı üretim takip sistemidir. Proje Python, Django, PostgreSQL ve Docker kullanılarak geliştirilmiştir. Docker kullanarak kolayca çalıştırılabilir ve geliştirme ortamı hızlıca kurulabilir.

## Gereksinimler

Proje çalıştırılmadan önce aşağıdaki yazılımların sisteminizde kurulu olduğundan emin olun:

- [Docker](https://www.docker.com/get-started) (Docker Desktop)
- [Git](https://git-scm.com/)
- [Python 3.11](https://www.python.org/downloads/) (Docker kullanmadan çalıştırmak için)

## Kurulum Adımları

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/erdemaltu/Python-Django-HavaAraciUretim.git
cd projeadi
```

### 2. Docker Kullanarak Projeyi Başlatma

Docker kullanarak projenizi çalıştırmak için şu adımları izleyin:

#### Docker Kullanarak Proje Çalıştırma

1. **Docker İmajlarını Oluşturun** ve konteynerleri başlatın:

   ```bash
   docker-compose up --build
   ```

2. **Veritabanı tablolarını oluşturun** (migration işlemi):

   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. **Superuser (Yönetici) oluşturun**:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

4. **Uygulamayı tarayıcıda görüntüleyin**:

   Tarayıcıda şu URL'yi açın: [http://localhost:8000](http://localhost:8000)

#### Docker Olmadan Projeyi Çalıştırma

1. **Sanal Ortam Oluşturun**:

   ```bash
   python -m venv env
   ```

2. **Sanal Ortamı Aktif Edin**:

   - **Windows**:
   
     ```bash
     .\env\scripts\activate
     ```

   - **MacOS / Linux**:
   
     ```bash
     source env/bin/activate
     ```

3. **Bağımlılıkları Yükleyin**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanı tablolarını oluşturun**:

   ```bash
   python manage.py migrate
   ```

5. **Superuser (Yönetici) oluşturun**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Geliştirme sunucusunu başlatın**:

   ```bash
   python manage.py runserver
   ```

7. **Uygulamayı tarayıcıda görüntüleyin**:
   
   Tarayıcıda şu URL'yi açın: [http://localhost:8000](http://localhost:8000)

### 3. PostgreSQL Kullanımı

Projede Docker PostgreSQL veritabanı kullanmaktadır. `docker-compose.yml` dosyasındaki ortam değişkenlerini düzenleyerek veritabanı yapılandırmalarını değiştirebilirsiniz:

```yaml
db:
  image: postgres:13
  environment:
    POSTGRES_DB: hava_araci_uretim_db
    POSTGRES_USER: mydbuser
    POSTGRES_PASSWORD: mydbpassword
  ports:
    - "5432:5432"
```

### 4. Projeyi Geliştirmek

Projeyi geliştirirken aşağıdaki komutları kullanabilirsiniz:

- **Statik dosyaları toplama**:

  ```bash
  docker-compose exec web python manage.py collectstatic
  ```

- **Birim testleri çalıştırma**:

  ```bash
  docker-compose exec web python manage.py test
  ```

### 5. Proje İçeriği

- **Django**: Python tabanlı web framework
- **PostgreSQL**: Veritabanı
- **Docker**: Konteynerizasyon
- **Docker Compose**: Servislerin orkestrasyonu

### 6. Sorun Giderme

- **Port Çakışması**: Eğer PostgreSQL 5432 portunda başka bir uygulama çalışıyorsa, `docker-compose.yml` dosyasındaki portu değiştirin.
- **CSRF Hataları**: Eğer form gönderimleri sırasında CSRF hatası alıyorsanız, CSRF token'ının düzgün bir şekilde ayarlandığından emin olun.

### 7. Katkıda Bulunma

Projeye katkıda bulunmak için lütfen şu adımları izleyin:

1. Fork'layın
2. Yeni bir branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push'layın (`git push origin feature/AmazingFeature`)
5. Bir pull request açın
