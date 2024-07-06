from django.test import TestCase
from account.models import User, Otp


class TestModelsAccount(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(phone_number='09191234567', password='123')

    def test_str(self):
        self.assertEqual(str(self.user), '09191234567')


