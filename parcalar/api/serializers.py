from rest_framework import serializers
from parcalar.models import Parca

class ParcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parca
        fields = ['id', 'isim', 'ucak_turu', 'parca_turu', 'stok_sayisi', 'geri_donusen']
