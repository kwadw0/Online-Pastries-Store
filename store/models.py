from webbrowser import get
from django.urls import reverse
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200,)
    price = models.DecimalField(max_digits=4,  decimal_places=2)
    images = models.ImageField(upload_to='covers/', blank=True)
    id = models.URLField(primary_key=True, default=uuid.uuid4,  editable=False,)
    description = models.TextField(max_length=250,)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args =[str(self.id)])

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.IntegerField()

    def __str__(self):
        return self.customer

class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
# Create your models here.
