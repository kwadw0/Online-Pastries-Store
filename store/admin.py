from django.contrib import admin
from .models import Product, Cart, CartItems, Customer

#how to display the objects in the admin panel 
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)

class CartAdmin(admin.ModelAdmin):
    list_display = ("date", "completed", "transaction_id",)


admin.site.register(Customer)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
admin.site.register(Product,ProductAdmin)


# Register your models here.
