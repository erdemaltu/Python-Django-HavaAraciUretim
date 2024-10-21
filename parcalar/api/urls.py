from django.urls import path, include
from .views import ParcaViewSet

urlpatterns = [
    path('parcalar/', ParcaViewSet.as_view({'get': 'list'})),
    path('parcalar/<int:pk>/', ParcaViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]
