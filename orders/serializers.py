

from rest_framework import serializers
from .models import OrderItem, Order
from django.db import transaction

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

        # On utilise transaction.atomic pour éviter les stocks fantômes
        with transaction.atomic():
            order = Order.objects.create(user=user)

            for item_data in orders_data:
                product = item_data['product']
                quantity_ordered = item_data['quantity']

                # Vérification : est-ce qu'on a assez de produits ?
                if product.quantity < quantity_ordered:
                    raise serializers.ValidationError(
                        f"Stock insuffisant pour {product.name}. Dispo: {product.quantity}"
                    )

                # MISE À JOUR DU STOCK (Soustraction et sauvegarde)
                product.quantity -= quantity_ordered
                product.save()

                # Création de l'article de commande
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity_ordered,
                    price=product.price
                )
            
            return order