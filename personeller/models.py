from django.db import models
from django.contrib.auth.models import AbstractUser
from takimlar.models import Takim

class Personel(AbstractUser):
    takim = models.ForeignKey(Takim, on_delete=models.CASCADE, related_name="personeller", null=True, blank=True)

    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personeller'

    def __str__(self):
        return self.username
