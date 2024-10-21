from django.db import models
from takimlar.models import Takim

class Parca(models.Model):
    UC_TUR = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    ]

    PARCA_TUR = [
        ('kanat', 'Kanat'),
        ('govde', 'Gövde'),
        ('kuyruk', 'Kuyruk'),
        ('aviyonik', 'Aviyonik'),
    ]
    
    isim = models.CharField(max_length=100)
    ucak_turu = models.CharField(max_length=10, choices=UC_TUR)
    parca_turu = models.CharField(max_length=50, choices=PARCA_TUR)
    stok_sayisi = models.IntegerField(default=0)
    geri_donusen = models.IntegerField(default=0)  # Geri dönüşüme gönderilen sayısı

    def __str__(self):
        return f"{self.ucak_turu} - {self.parca_turu}"

