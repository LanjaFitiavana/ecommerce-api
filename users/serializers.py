from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfil


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model = User
        fields = ['id','username','password','email']

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
        

class ProfilSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only = True,)
    email = serializers.EmailField(source='user.email',read_only = True,)

    class Meta:
        model = UserProfil
        fields = ['id','username','email','bio','adress','number','city','country']