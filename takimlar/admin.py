from django.contrib import admin
from .models import Takim

@admin.register(Takim)
class TakimAdmin(admin.ModelAdmin):
    list_display = ('isim', 'parca_turu')
