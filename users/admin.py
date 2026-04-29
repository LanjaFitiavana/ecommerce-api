from django.contrib import admin
from .models import UserProfil

@admin.register(UserProfil)

class UserAdmin(admin.ModelAdmin):
    list_display = ['user','city','country']
    list_filter = ['city']
    
