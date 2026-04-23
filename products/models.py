from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images',null=True,blank = True)
    descriptions = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ="Product"
        verbose_name_plural ="Products"
        ordering = ['-created_at']
    
    @property
    def is_in_stock(self):
        return self.quantity > 0