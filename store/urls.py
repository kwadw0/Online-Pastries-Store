from django.urls import path
from .views import StoreListView


# urls for the view methods.
urlpatterns = [path('', StoreListView.as_view(), name='store'),]