from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    list_display=('email','username',)

admin.site.register(CustomUser,CustomUserAdmin)