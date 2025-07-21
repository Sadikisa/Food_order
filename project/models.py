from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Restaurant(models.Model):
    restaurant_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    addres=models.CharField(max_length=120)
    user = models.ManyToManyField(User)

class Order(models.Model):

   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    food=models.CharField(max_length=120,default=True)
    drink=models.CharField(max_length=120,default=True)
    sos1=models.CharField(max_length=120,default=False)
    sos2=models.CharField(max_length=120,default=False)
    desc=models.TextField(default=True)
    adet=models.IntegerField()
    price=models.IntegerField()

    snack=models.BooleanField(null=True)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=225)


class Supplier(models.Model):

    supplier_id=models.CharField(max_length=20,primary_key=True)
    supplier_name=models.CharField(max_length=25)
    delivery= models.ManyToManyField(Restaurant)