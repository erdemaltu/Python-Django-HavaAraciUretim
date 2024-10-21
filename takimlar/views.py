from rest_framework import viewsets
from takimlar.models import Takim
from .serializers import TakimSerializer

class TakimViewSet(viewsets.ModelViewSet):
    queryset = Takim.objects.all()
    serializer_class = TakimSerializer
