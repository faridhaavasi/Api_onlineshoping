from django.urls import path
from .import views
from .views import OrderItemViewApi
from rest_framework.routers import DefaultRouter

app_name = 'order'
urlpatterns = [
    path('cart', views.CartViewApi.as_view(), name='cart'),
    path('cartadd', views.CartAddViewApi.as_view(), name='cart_add'),
    path('cartremove/<int:product_id>', views.CartRemoveViewApi.as_view(), name='cart_remove'),
    path('addorder', views.AddOrderViewApi.as_view(), name='add_order'),
]

router = DefaultRouter()
router.register(r'order_items', OrderItemViewApi, basename='order_item')
urlpatterns += router.urls