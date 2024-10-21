from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from parcalar.models import Parca
from envanter.models import Envanter
from .serializers import ParcaSerializer

class ParcaViewSet(viewsets.ModelViewSet):
    serializer_class = ParcaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_team = self.request.user.takim  # Kullanıcının takımı
        # Eğer kullanıcının takımı yoksa hata döndür
        if user_team is None:
            return Parca.objects.none()  # Boş bir sorgu döndür, sistemdeki parçaları göstermemek için

        # Montaj takımı dışındaki takımlar kendi parçalarını görebilir
        if user_team.isim in ['Kanat Takımı', 'Gövde Takımı', 'Kuyruk Takımı', 'Aviyonik Takımı']:
            return Parca.objects.filter(parca_turu=user_team.parca_turu)

        # Montaj takımı ise uçak işlemleriyle ilgilenir, parça gösterilmez
        if user_team.isim == 'Montaj Takımı':
            return Parca.objects.none()  # Montaj takımı parça göremez

        # Varsayılan olarak boş bir sorgu döndür
        return Parca.objects.none()
    
    def update(self, request, *args, **kwargs):
        user_team = request.user.takim
        parca = self.get_object()

        # Kullanıcının takımına ait olmayan bir parçayı güncellemeye çalışıyorsa hata ver
        if parca.parca_turu != user_team.parca_turu:
            return Response({"error": "Bu parçayı güncelleme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)

        # Stok miktarını +1 olarak güncelle
        parca.stok_sayisi += 1
        parca.save()

        return Response({"message": f"{parca.parca_turu} stok miktarı güncellendi. Yeni stok: {parca.stok_sayisi}"}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user_team = request.user.takim
        parca = self.get_object()

        # Kullanıcının takımına ait olmayan bir parçayı geri dönüştürmeye çalışıyorsa hata ver
        if parca.parca_turu != user_team.parca_turu:
            return Response({"error": "Bu parçayı geri dönüştürme yetkiniz yok."}, status=status.HTTP_403_FORBIDDEN)

        # Stok sıfırsa geri dönüşüm yapılamaz, hata döndür
        if parca.stok_sayisi <= 0:
            return Response({"error": f"{parca.parca_turu} parçası için stok yetersiz."}, status=status.HTTP_400_BAD_REQUEST)

        # Stok miktarını -1 olarak güncelle
        parca.stok_sayisi -= 1
        parca.geri_donusen += 1
        parca.save()

        return Response({"message": f"{parca.parca_turu} geri dönüştürüldü. Yeni stok: {parca.stok_sayisi}, Geri dönüştürülen: {parca.geri_donusen}"}, status=status.HTTP_200_OK)

