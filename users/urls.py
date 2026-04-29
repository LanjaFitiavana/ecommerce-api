from django.urls import path,include
from .views import UserView,ListUser,Profil
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = DefaultRouter()
router.register(r'profil',Profil,basename='profil')
#router.register(r'register',UserView,basename='register')
#router.register(r'login',TokenObtainPairView,basename='login')

urlpatterns = [
    path('register/',UserView.as_view(),name = 'register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('list/',ListUser.as_view(),name='list'),
    path('',include(router.urls))
]
