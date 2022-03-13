from django.contrib import admin
from .models import Product

#how to display the objects in the admin panel 
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)

admin.site.register(Product, ProductAdmin)
# Register your models here.
