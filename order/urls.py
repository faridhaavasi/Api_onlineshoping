from django.urls import path
from .import views


app_name = 'order'
urlpatterns = [
    path('cart', views.CartViewApi.as_view(), name='cart'),
]
