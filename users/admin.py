from django.contrib import admin

from . forms import CustomUserChangeForm,CustomUserCreationForm
from . models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    form=CustomUserChangeForm
    add_form=CustomUserCreationForm

admin.site.register(CustomUser,CustomUserAdmin)
