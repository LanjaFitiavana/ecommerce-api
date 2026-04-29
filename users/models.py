from django.db import models
from django.contrib.auth.models import User


class UserProfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil')
    bio = models.TextField(max_length=5000,blank=True)
    adress = models.CharField(max_length=400,blank=True)
    number = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=500,blank=True)
    country = models.CharField(max_length=100,blank=True)
    
    class Meta:
        verbose_name = "UserProfil"
        verbose_name_plural = "UserProfils"
