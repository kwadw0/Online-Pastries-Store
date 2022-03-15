from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

class StoreListView(ListView):
    model = Product
    template_name = 'store.html'
# Create your views here.
