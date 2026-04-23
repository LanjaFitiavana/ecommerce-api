from django.urls import path
from .views import OrderCreateApiview


urlpatterns = [
    path('',OrderCreateApiview.as_view(),name='create')
]
