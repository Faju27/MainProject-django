from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LoginView(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(LoginView, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)


class Seller(models.Model):
    user = models.ForeignKey(LoginView, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    document = models.FileField(upload_to='document') #26/12/24
    # photo = models.ImageField(upload_to='image')

