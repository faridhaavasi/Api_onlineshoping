from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import RegisterApiView, VerifyCodeApi



class Testurls(SimpleTestCase):
    def test_registerApiView_url_name(self):
        url = reverse('accounts:register_user')
        url_name = resolve(url).url_name

        self.assertEqual(url_name, 'register_user')

    def test_VerifycodeApi_url_name(self):
        url = reverse('accounts:verify code')
        url_name = resolve(url).url_name

        self.assertEqual(url_name, 'verify code')




