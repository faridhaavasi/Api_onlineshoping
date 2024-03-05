from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from .models import User

class RegisterApiView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            request.session['register_info'] = {}
            session_info_register = request.session['register_info']
            session_info_register = {
                'email': validated_data['email'],
                'first_name': validated_data['first_name'],
                'last_name': validated_data['last_name'],
                'phone_number': validated_data['phone_number'],
                'password': validated_data['password']
            }
            return Response(session_info_register)
        return Response(serializer.errors)



