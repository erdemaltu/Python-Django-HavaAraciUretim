from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):#kullanıcı giriş işlemi için htmle form gönderimi için
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'UserName or Email',
        'id':'username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'id':'password'
    }))