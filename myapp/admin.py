# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Patient,Doctor

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('is_patient', 'is_doctor', 'address_line1', 'city', 'state', 'pincode')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)