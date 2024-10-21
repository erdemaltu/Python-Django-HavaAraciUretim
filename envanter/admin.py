from django.contrib import admin
from .models import Envanter

class EnvanterAdmin(admin.ModelAdmin):
    list_display = ('ucak_turu', 'stok_miktari', 'kanat_gereksinimi', 'govde_gereksinimi', 'kuyruk_gereksinimi', 'aviyonik_gereksinimi')
    search_fields = ('ucak_turu',)  # Uçak türüne göre arama yapılabilmesi için

admin.site.register(Envanter, EnvanterAdmin)
