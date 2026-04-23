from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ['name','price','quantity','is_in_stock']
    list_filter = ['created_at']