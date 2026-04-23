"""
from rest_framework import serializers
from .models import OrderItem,Order


class SerializerOrderItem(serializers.ModelSerializer):
    price_total = serializers.ReadOnlyField(source='get_total_items')
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = OrderItem
        fields = ['id','product','price','price_total','quantity']

class SerializerOrder(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source = 'user.username') 
    all_price = serializers.ReadOnlyField(source = 'get_cart_total')
    orders = SerializerOrderItem(many=True)
    class Meta:
        model = Order
        fields = ['id','created_at','user_name','all_price','orders']
        read_only_fields = ['user_name','all_price']

    def create(self,validated_data):
        orders_data = validated_data.pop('orders')
        user = self.context['request'].user
        order = Order.objects.create(user=user,**validated_data)
        
        for item_data in orders_data:
            product = item_data['product']
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity = item_data['quantity'],
                price = product.price)
        return order
 """   

from rest_framework import serializers
from .models import OrderItem, Order

class SerializerOrderItem(serializers.ModelSerializer):
    price_total = serializers.ReadOnlyField(source='get_total_items')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'price_total', 'quantity']
        read_only_fields = ['price']  

class SerializerOrder(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    all_price = serializers.ReadOnlyField(source='get_cart_total')
    orders = SerializerOrderItem(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'user_name', 'all_price', 'orders']

    def validate_orders(self, value):
        if not value:
            raise serializers.ValidationError("La commande doit contenir au moins un article.")
        return value

    def create(self, validated_data):
        orders_data = validated_data.pop('orders')
        user = self.context['request'].user
        order = Order.objects.create(user=user)

        for item_data in orders_data:
            product = item_data['product']
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data['quantity'],
                price=product.price  
            )
        return order