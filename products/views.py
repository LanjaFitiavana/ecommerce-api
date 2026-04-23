from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Product
from .serializers import ProductSerializer
from .pagination import MyPage

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering = ["-created_at"]
    pagination_class = MyPage