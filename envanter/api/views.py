from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from envanter.models import Envanter
from .serializers import EnvanterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from parcalar.models import Parca

class EnvanterViewSet(viewsets.ModelViewSet):
    serializer_class = EnvanterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Sadece montaj takımı uçakları listeleyebilir
        user_team = self.request.user.takim
        if user_team.isim == 'Montaj Takımı':
            return Envanter.objects.all()  # Montaj takımı tüm uçakları görebilir
        return Envanter.objects.none()  # Diğer takımlar için liste boş

class UcakUretimiUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user_team = request.user.takim

        # Sadece montaj takımı üretim yapabilir
        if user_team.isim != 'Montaj Takımı':
            return Response({"error": "Bu işlemi yapma yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)

        ucak_id = kwargs.get('pk')  # Uçak ID'si URL'den alınır
        try:
            envanter = Envanter.objects.get(id=ucak_id)
        except Envanter.DoesNotExist:
            return Response({"error": "Uçak envanterde bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

        # Uçak üretimi için gerekli parçalar
        eksik_parcalar = []

        # Kanat stok kontrolü
        kanat = Parca.objects.filter(parca_turu='kanat', ucak_turu=envanter.ucak_turu).first()
        if not kanat or kanat.stok_sayisi < envanter.kanat_gereksinimi:
            eksik_parcalar.append('Kanat')

        # Gövde stok kontrolü
        govde = Parca.objects.filter(parca_turu='govde', ucak_turu=envanter.ucak_turu).first()
        if not govde or govde.stok_sayisi < envanter.govde_gereksinimi:
            eksik_parcalar.append('Gövde')

        # Kuyruk stok kontrolü
        kuyruk = Parca.objects.filter(parca_turu='kuyruk', ucak_turu=envanter.ucak_turu).first()
        if not kuyruk or kuyruk.stok_sayisi < envanter.kuyruk_gereksinimi:
            eksik_parcalar.append('Kuyruk')

        # Aviyonik stok kontrolü
        aviyonik = Parca.objects.filter(parca_turu='aviyonik', ucak_turu=envanter.ucak_turu).first()
        if not aviyonik or aviyonik.stok_sayisi < envanter.aviyonik_gereksinimi:
            eksik_parcalar.append('Aviyonik')

        # Eksik parçalar varsa hata döndür
        if eksik_parcalar:
            return Response({"error": f"Stokta eksik parçalar var: {', '.join(eksik_parcalar)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Parçalar stoktan düşürülüyor
        kanat.stok_sayisi -= envanter.kanat_gereksinimi
        kanat.save()

        govde.stok_sayisi -= envanter.govde_gereksinimi
        govde.save()

        kuyruk.stok_sayisi -= envanter.kuyruk_gereksinimi
        kuyruk.save()

        aviyonik.stok_sayisi -= envanter.aviyonik_gereksinimi
        aviyonik.save()

        # Uçak envantere ekleniyor
        envanter.stok_miktari += 1
        envanter.save()

        return Response({"message": f"{envanter.ucak_turu} başarıyla üretildi ve stok güncellendi."}, status=status.HTTP_200_OK)

