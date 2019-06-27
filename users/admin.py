from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import EmailUserCreationForm
from .models import EmailUser

class CustomUserAdmin(UserAdmin):
    add_form = EmailUserCreationForm
    form = EmailUserCreationForm
    model = EmailUserCreationForm
    list_display = ['email',]

admin.site.register(EmailUser, CustomUserAdmin)