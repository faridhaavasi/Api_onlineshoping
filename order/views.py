from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer
import json
from .cart import Cart


class CartViewApi(APIView):
    serializer_class = CartSerializer

    def get(self, request):
        cart = Cart(request)

        ser = self.serializer_class(cart)
        return Response(ser.data)
