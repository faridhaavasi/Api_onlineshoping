from django.test import TestCase, Client, RequestFactory
from account.models import User, Otp
from account.views import RegisterApiView, VerifyCodeApi
from account.serializer import RegisterSerializer, VerifyCodeSerializer
from django.urls import reverse

class TestAccountViews(TestCase):
    def setUp(self):
        self.client = Client()

    def Test_registerApiViewValidPostMethod(self):
        ser = RegisterSerializer(data=
        {
            'phone_number': '09191234567',
            'email': 'farid@gmaul.com',
            'first_name': 'farid',
            'last_name': 'havasi',
            'password': '1111'
        }
        )
        req = self.client.post(reverse('accounts:register_user'), data=ser.data)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(User.objects.count(),1)


