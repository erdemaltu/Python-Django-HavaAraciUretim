from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from personeller.models import Personel
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from functools import wraps

#NOT:Veri ile alakalı işlemlerin hepsi html sayfalarında jquary ile yapılmıştır, sadece örnek olması açısından kiralamaların olduğu sayfada sadece kiralanlar listesi ve kullanıcı çıkış işlemi view üzerinden yapılmıştır
def takim_izinleri_gerekli(takim_adi):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.takim and request.user.takim.isim == takim_adi:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Bu sayfaya erişim yetkiniz yok.")
        return _wrapped_view
    return decorator

def index(request):#anasayfa view'i
    
    return render(request, 'index.html')#html sayfa görüntülemesi

@login_required(login_url='/login')
def iha_list(request):#ihalar view'i
    
    return render(request, 'ihalar.html')

@login_required(login_url='/login')
def kiralama_list(request):#kiralamalar view'i

    uyeler = Personel.objects.all()
    context = {
        'uyeler':uyeler,
    }
    return render(request, 'kiralama.html', context)

def user_login(request):#kullanıcı giriş view'i
    form = LoginForm()

    return render (request, 'login.html', {'form':form})

def user_logout(request):#kullanıcı çıkış view'i
    logout(request)
    return redirect('index')

def parca_dashboard(request):
    return render(request, 'parca_dashboard.html')

@takim_izinleri_gerekli('Montaj Takımı')
def montaj_dashboard(request):
    return render(request, 'montaj_dashboard.html')

