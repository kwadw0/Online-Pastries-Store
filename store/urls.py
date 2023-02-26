from django.urls import path
from .views import StoreListView, StoreDetailView, CartListView


# urls for the view methods.
urlpatterns = [
    path('', StoreListView.as_view(), name='store'),
    path('cart/', CartListView.as_view(), name="cart"),
    path('<uuid:pk>', StoreDetailView.as_view(), name='product_detail'),
]