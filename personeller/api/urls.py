from django.urls import path
from personeller.api import views as api_views

urlpatterns = [
    path('login/', api_views.user_login, name='login'),#giriş yapma api urlsi
    path('logout/', api_views.user_logout, name='logout'),#çıkış yapma api urlsi
]
