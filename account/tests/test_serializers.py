from django.test import TestCase
from account.serializer import RegisterSerializer, VerifyCodeSerializer



class TestSerializer(TestCase):
    def test_RegisterSerializer_is_valid(self):
        ser = RegisterSerializer(data={'email': 'farid@gmail.com', 'first_name': 'farid',
                                       'last_name': 'havasi', 'phone_number': '09191234567',
                                       'password': '1111'})
        self.assertTrue(ser.is_valid())

    def test_RegisterSerializer_is_not_valid(self):
        ser = RegisterSerializer(data={'email': 'farid@gmail.com', 'first_name': 'farid',
                                       'last_name': 'havasi', 'phone_number': '09191234567111',
                                       'password': '1111'})
        self.assertFalse(ser.is_valid())
        self.assertEqual(len(ser.errors), 1)

class TestVerifyCodeSerializer(TestCase):
    def test_VerifyCodeSerializer_is_valid(self):
        ser = VerifyCodeSerializer(data={'code': '1234'})
        self.assertTrue(ser.is_valid())

    def test_int_VerifyCodeSerializer_is_valid(self):
        ser = VerifyCodeSerializer(data={'code': 1234})
        self.assertTrue(ser.is_valid())