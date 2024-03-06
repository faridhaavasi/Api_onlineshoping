from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework import status
from random import randint
from .models import User, Otp

class RegisterApiView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            random_code = randint(1000,9999)

            request.session['register_info'] = {}
            session_info_register = request.session['register_info']
            session_info_register = {
                'email': validated_data['email'],
                'first_name': validated_data['first_name'],
                'last_name': validated_data['last_name'],
                'phone_number': validated_data['phone_number'],
                'password': validated_data['password'],
                'random_code': random_code
            }
            Otp.objects.create(phone_number=validated_data['phone_number'], code=random_code)
            return Response({'data':session_info_register}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

