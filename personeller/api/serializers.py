from rest_framework import serializers
from personeller.models import Personel

class UserSerializer(serializers.ModelSerializer):#Kullanıcı modeli için dönüştürücü
    class Meta:
        model = Personel
        fields = ['id','username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Personel(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user