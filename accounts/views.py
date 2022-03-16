from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class SignUpViewPage(generic.CreateView):
    form = CustomUserCreationForm
    success_url = reverse_lazy('store')
    template_name = 'signup.html'
# Create your views here.
