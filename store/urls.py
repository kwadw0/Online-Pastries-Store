from django.urls import path
from .views import StoreListView, StoreDetailView


# urls for the view methods.
urlpatterns = [
    path('', StoreListView.as_view(), name='store'),
    path('<uuid:pk>', StoreDetailView.as_view(), name='product_detail'),
]