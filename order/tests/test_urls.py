from django.test import SimpleTestCase
from django.urls import reverse, resolve
from order.views import AddOrderViewApi, CartViewApi, CartRemoveViewApi, CartAddViewApi



class TestOrderUrl(SimpleTestCase):
    def setUp(self):
        self.AddOrderApiViewUrl = reverse('order:add_order')
        self.CartViewApiUrl = reverse('order:cart')
        self.CartAddApiViewUrl = reverse('order:cart_add')
        self.CartRemoveApiViewUrl = reverse('order:cart_remove')
    def test_AddOrderApiViewUrl(self):
        view = resolve(self.AddOrderApiViewUrl).func.view_class
        self.assertEqual(view, AddOrderViewApi)
