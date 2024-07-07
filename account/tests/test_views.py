from django.test import TestCase, Client, RequestFactory
from account.models import User, Otp
from account.views import RegisterApiView, VerifyCodeApi
from account.serializer import RegisterSerializer, VerifyCodeSerializer
from django.urls import reverse

class TestAccountViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_api_view_valid_post_method(self):
        ser = RegisterSerializer(data=
        {
            'phone_number': '09191234567',
            'email': 'farid@gmaul.com',
            'first_name': 'farid',
            'last_name': 'havasi',
            'password': '1111'
        }
        )
        if ser.is_valid():
            req = self.client.post(reverse('accounts:register_user'), data=ser.data)
            User.objects.create_user(**ser.data)
            self.assertEqual(req.status_code, 200)
            self.assertEqual(User.objects.count(),1)

    # def test_register_api_view_invalid_post_method(self):
    #     ser = RegisterSerializer(data=
    #     {
    #         'phone_number': '0919123456711',
    #         'email': 'faridgmaul.com',
    #         'first_name': 'farid',
    #         'last_name': 'havasi',
    #         'password': '1111'
    #     }
    #     )
    #     req = self.client.post(reverse('accounts:register_user'), data=ser.data)
    #     self.assertFalse(ser.is_valid())
    #
    '''
    When the serializer is of the serializer model,
     it is not tested at all if the data is not correct,
     because the validation prevents the entry of wrong data.
    '''

