"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SerializerOrder
from rest_framework import status
from .permissions import IsOwner
from .models  import Order

class OrderCreateApiview(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    
    def post(self,request):
        serializer = SerializerOrder(data=request.data,context = {
            'request':request
        })
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import SerializerOrder
from .models import Order

class OrderCreateApiview(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SerializerOrder

    def post(self, request):
        serializer = SerializerOrder(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = SerializerOrder(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    