"""
URL configuration for hava_araci_uretim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Hava Aracı Üretim API",
      default_version='v1',
      description="Hava aracı üretim takip API belgeleri",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/personeller/', include('personeller.api.urls')),
    path('api/takimlar/', include('takimlar.api.urls')),
    path('api/parcalar/', include('parcalar.api.urls')),
    path('api/envanter/', include('envanter.api.urls')),
    path('', include('frontend.urls')),  # Frontend uygulaması URL'leri
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

