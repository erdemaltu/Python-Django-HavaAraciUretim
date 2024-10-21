from django.urls import path
from .views import EnvanterViewSet, UcakUretimiUpdateAPIView

urlpatterns = [
    path('ucaklar/', EnvanterViewSet.as_view({'get': 'list'})),  # Uçakları listeleme (sadece montaj takımı)
    path('ucaklar/<int:pk>/', UcakUretimiUpdateAPIView.as_view(), name='ucak_uretimi_update'),  # Uçak üretim işlemi

]
