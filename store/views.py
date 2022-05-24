from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

#This tells the browser to display the products
class StoreListView(ListView):
    model = Product
    template_name = 'store.html'
#This tells the browser to display the detail products
class StoreDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
# Create your views here.
