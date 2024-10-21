from django.urls import path
from .views import PersonelTakimAPIView

urlpatterns = [
    path('personel', PersonelTakimAPIView.as_view(), name='personel-takim'),  # Takım bilgisi API'si
]
