from django.urls import path
from . import views

urlpatterns = [#front-end urlleri
    path('', views.index, name="index"),#anasayfa urlsi
    path('login/', views.user_login, name="log-in"),# kullanıcı giriş urlsi
    path('logout/', views.user_logout, name="log-out"),#kullanıcı çıkış urlsi
    # path('search/', views.search, name="search"),
    path('parca-dashboard/', views.parca_dashboard, name='parca_dashboard'),
    path('montaj-takimi-dashboard/', views.montaj_dashboard, name='montaj_dashboard'),
]