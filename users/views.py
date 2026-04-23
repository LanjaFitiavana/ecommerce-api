from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer,ListSerializer,ProfilSerializer
from rest_framework import viewsets,generics
from .models import UserPofil
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner



class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUser(generics.ListAPIView):
    permission_classes= [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ListSerializer

class Profil(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwner]
    queryset = UserPofil.objects.all()
    serializer_class = ProfilSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)