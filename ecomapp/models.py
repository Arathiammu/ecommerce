from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=255)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.IntegerField()
    image=models.ImageField(blank=True,upload_to="image/",null=True)

class Usermember(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to="image/",null=True)

class cart1(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)

class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    number=models.CharField(max_length=10)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)

class Book(models.Model):
    isbn=models.CharField(max_length=17)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    quantity=models.IntegerField()
    email=models.EmailField()
    number=models.CharField(max_length=10)
