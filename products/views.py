from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Product
from .serializers import ProductSerializer
from .pagination import MyPage
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering = ["-created_at"]
    pagination_class = MyPage