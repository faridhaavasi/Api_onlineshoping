from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'accounts'
urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register', views.RegisterApiView.as_view(), name='register_user'),
    path('api/verify', views.VerifyCodeApi.as_view(), name='verify code'),
]
