from django.test import TestCase
from order.models import Order, OrderItem, Coupon
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()
class TestOrderModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number='08108548640', password='111234')
        self.user_id = User.objects.get(id=1)
        self.order = Order.objects.create(user=self.user_id, paid=True)
    def test_order_model(self):
        self.assertEqual(str(self.order), f'{self.order.user}- True')



    # It is not reasonable to write a test for all models

