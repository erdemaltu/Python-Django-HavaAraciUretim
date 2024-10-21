from django.db import models

class Envanter(models.Model):
    UC_TUR = [
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    ]

    ucak_turu = models.CharField(max_length=10, choices=UC_TUR)
    stok_miktari = models.IntegerField(default=0)
    kanat_gereksinimi = models.IntegerField(default=2)
    govde_gereksinimi = models.IntegerField(default=1)
    kuyruk_gereksinimi = models.IntegerField(default=1)
    aviyonik_gereksinimi = models.IntegerField(default=1)

    def __str__(self):
        return self.ucak_turu
