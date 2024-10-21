from django.db import models

class Takim(models.Model):
    TAKIM_TUR = [
        ('kanat', 'Kanat Takımı'),
        ('govde', 'Gövde Takımı'),
        ('kuyruk', 'Kuyruk Takımı'),
        ('aviyonik', 'Aviyonik Takımı'),
        ('montaj', 'Montaj Takımı')
    ]
    
    isim = models.CharField(max_length=100)
    parca_turu = models.CharField(max_length=50, choices=TAKIM_TUR)

    def __str__(self):
        return self.isim

