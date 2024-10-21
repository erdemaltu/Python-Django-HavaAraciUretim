from rest_framework import serializers
from envanter.models import Envanter

class EnvanterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envanter
        fields = ['id', 'ucak_turu', 'stok_miktari', 'kanat_gereksinimi', 'govde_gereksinimi', 'kuyruk_gereksinimi', 'aviyonik_gereksinimi']
