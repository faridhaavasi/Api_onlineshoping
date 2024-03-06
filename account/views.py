from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer, VerifyCodeSerializer
from rest_framework import status
from random import randint
from .models import User, Otp


class RegisterApiView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            random_code = randint(1000, 9999)

            request.session['register_info'] = {
                'email': validated_data['email'],
                'first_name': validated_data['first_name'],
                'last_name': validated_data['last_name'],
                'phone_number': validated_data['phone_number'],
                'password': validated_data['password'],
                'random_code': random_code
            }
            session_info_register = request.session['register_info']
            Otp.objects.create(phone_number=validated_data['phone_number'], code=random_code)
            return Response({'data': session_info_register}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class VerifyCodeApi(APIView):
    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            session_register_info = request.session['register_info']
            phone_number = session_register_info['phone_number']
            otp = Otp.objects.get(phone_number=phone_number)
            instance_code = otp.code

            if instance_code == validated_data['code']:
                session_register_info = request.session['register_info']

                User.objects.create_user(
                    email=session_register_info['email'],
                    phone_number=session_register_info['phone_number'],
                    first_name=session_register_info['first_name'],
                    last_name=session_register_info['last_name'],
                    password=session_register_info['password']
                )
                otp.delete()
                del session_register_info

                return Response({'massage': ' you are register'}, status=status.HTTP_200_OK)
            return Response({'massage': 'code is not match'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
