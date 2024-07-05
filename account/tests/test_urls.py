from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import RegisterApiView, VerifyCodeApi


class Testurls(SimpleTestCase):
    def setUp(self):
        self.register_url = reverse('accounts:register_user')
        self.veryfi_url = reverse('accounts:verify code')


    def test_registerApiView_url_name(self):
        url_name = resolve(self.register_url).url_name
        self.assertEqual(url_name, 'register_user')

    def test_VerifycodeApi_url_name(self):
        url_name = resolve(self.veryfi_url).url_name
        self.assertEqual(url_name, 'verify code')

    def test_RegisterApiView(self):
        view = resolve(self.register_url).func.view_class
        self.assertEqual(view, RegisterApiView)


    def test_veryfiCodeApiView(self):
        view = resolve(self.veryfi_url).func.view_class
        self.assertEqual(view, VerifyCodeApi)


