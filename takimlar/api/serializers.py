from rest_framework import serializers
from takimlar.models import Takim

class TakimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takim
        fields = ['id', 'isim', 'parca_turu']
