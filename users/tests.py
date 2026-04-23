from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserPofil
from datetime import timedelta

class TestLogin(APITestCase):
    def setUp(self):
        self.username = "testuer"
        self.password = "123456789"
        self.user = User.objects.create_user(
            username=self.username,
            password = self.password
        )
        self.login = reverse('login')
    
    def test_Great_Password(self):
        data = {
            "username":self.username,
            "password":self.password
        }
        response = self.client.post(self.login,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('access',response.data)
        self.assertIn('refresh',response.data)
        print(response.data)

    def test_Wrong_Password(self):
        data = {
            "username":self.username,
            "password":"bad_password"     
        }
        response = self.client.post(self.login,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

 
    

class TestRegister(APITestCase):
    register = reverse('register')

    def test_succesfuly(self):
        data = {
            "username": "testuser",
            "email":"test@gmail.com",
            "password":"0123456789"
        }

        response = self.client.post(self.register,data,rformat='json')
        print(response.data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)





class Test_List(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="pass123",
            email="test@gmail.com"
        )
        self.urls = reverse('list')
    
    def test_jwt_acces_token(self):
        refresh =  RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)


        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print(response.data)

    def test_expire_token(self):
        refresh = RefreshToken.for_user(self.user)
        access = refresh.access_token

        access.set_exp(lifetime=timedelta(seconds=-10))
        expired_token = str(access)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {expired_token}')
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_bad_token(self):
        self.client.credentials(HTTP_AUTHORIZATION= 'Bearer faketoken1233')
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)



class TestProfilIsowner(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user('owner',password='pass123',email='owner@gmail.com')
        self.other = User.objects.create_user('other',password='pass34567',email='other@gmail.com')

        self.account = UserPofil.objects.create(
            user = self.owner,
            bio = "i am there",
            adress ="lto pres",
            number = "01234",
            city ="Tana",
            country = "mada"
        )
        #self.urls = reverse('profil-list')
        self.urls = reverse('profil-detail',kwargs={'pk':self.account.pk})

    def test_owner_update(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.urls,{'bio':'okay'})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_other_update(self):
        self.client.force_authenticate(user=self.other)
        response = self.client.patch(self.urls,{'bio':'sorry'})
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_owner_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.urls)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_other_delete(self):
        self.client.force_authenticate(user=self.other)
        response = self.client.delete(self.urls)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_no_auth(self):
        response = self.client.patch(self.urls,{'title':'test'})
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_owner_jwt(self):
        refresh = RefreshToken.for_user(self.owner)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.patch(self.urls,{'title':'via jwt'})
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        print(response.data)