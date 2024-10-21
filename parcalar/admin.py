from django.contrib import admin
from .models import Parca

@admin.register(Parca)
class ParcaAdmin(admin.ModelAdmin):
    list_display = ('isim', 'ucak_turu', 'parca_turu', 'stok_sayisi', 'geri_donusen')
