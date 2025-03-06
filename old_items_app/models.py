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
    document = models.FileField(upload_to='document')  # 26/12/24
    # photo = models.ImageField(upload_to='image')


class Product(models.Model):
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=3)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    photo = models.FileField(upload_to='product_photo/')


class Cart(models.Model):
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)


class MyStatus(models.Model):
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Chat(models.Model):
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)
    status_details = models.ForeignKey(MyStatus, on_delete=models.CASCADE)
    customer_message = models.CharField(max_length=100, null=True, blank=True)
    seller_message = models.CharField(max_length=100, null=True, blank=True)
    date_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer_comment = models.CharField(max_length=100, null=True, blank=True)
    seller_comment = models.CharField(max_length=100, null=True, blank=True)
    date_time = models.DateTimeField(auto_now=True)


