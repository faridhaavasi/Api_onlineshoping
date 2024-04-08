from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartAddSerializer, CartRemoveSerializer
from product.models import Product
from .cart import Cart


class CartViewApi(APIView):

    def get(self, request):
        cart = Cart(request)
        return Response(request.session.get('cart'), status=status.HTTP_200_OK)


class CartAddViewApi(APIView):
    serializer_class = CartAddSerializer

    def post(self, request):
        cart = Cart(request)
        ser = self.serializer_class(data=request.POST)
        if ser.is_valid():
            product = Product.objects.get(id=ser.validated_data['id_of_product'])
            cart.add(product, quantity=ser.validated_data['quantity'])
            return Response({'massage': 'added'}, status=status.HTTP_201_CREATED)
        return Response(ser.errors)
class CartRemoveViewApi(APIView):
    serializer_class = CartRemoveSerializer
    def get(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.remove(product=product)
        return Response({'massage': 'deleted'}, status=status.HTTP_200_OK)
