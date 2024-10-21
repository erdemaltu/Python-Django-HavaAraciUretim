from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Personel

class PersonelAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'takim')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'takim'),
        }),
    )

admin.site.register(Personel, PersonelAdmin)
