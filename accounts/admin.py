from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
