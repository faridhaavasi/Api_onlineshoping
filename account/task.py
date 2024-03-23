from celery import shared_task
from .models import Otp
from django.utils import timezone

shared_task()
def remove_expired_otp_code():
    """
    delete all otp code is created in 2 min ago

    """
    tow_min_ago = timezone.now() - timezone.timedelta(minutes=2)
    Otp.objects.filter(created__lt=tow_min_ago).delete()
    return True
