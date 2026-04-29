from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    is_in_stock = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ['id','name','price','quantity','image','descriptions','is_in_stock','created_at','updated_at']
        read_only_fields = ['id','is_in_stock','created_at','updated_at']

    def validate_quantity(self,value):
        if value < 0:
            raise serializers.ValidationError('The quantity must be non negative')
        return value
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('The price must be grater than or equal to 0')
        return value