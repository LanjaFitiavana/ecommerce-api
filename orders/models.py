from django.db import models
#from django.contrib.auth import get_user_model
from products.models import Product
from django.contrib.auth.models import User
#User = get_user_model


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    created_at= models.DateTimeField(auto_now_add=True)

    @property
    def get_cart_total(self):
        orders = self.orders.all()
        total = 0
        total = sum([order.get_total_items for order in orders])
        return total

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orders')
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='product')
    price = models.DecimalField(max_digits=10,decimal_places=3)
    quantity = models.PositiveIntegerField(default=1) 


    @property
    def get_total_items(self):
        return self.price * self.quantity