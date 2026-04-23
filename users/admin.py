from django.contrib import admin
from .models import UserPofil

@admin.register(UserPofil)

class UserAdmin(admin.ModelAdmin):
    list_display = ['user','city','country']
    list_filter = ['city']
    
