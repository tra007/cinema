from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    fieldsets = UserAdmin.fieldsets + (
        ("None", {'fields': ('phoneNumber',)}),
    )