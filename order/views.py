from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import CartAddSerializer, CartRemoveAddOrderSerializer
from product.models import Product
from .models import Order, OrderItem
from .cart import Cart


class CartViewApi(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        cart = Cart(request)
        return Response(request.session.get('cart'), status=status.HTTP_200_OK)


class CartAddViewApi(APIView):
    serializer_class = CartAddSerializer
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        cart = Cart(request)
        ser = self.serializer_class(data=request.POST)
        if ser.is_valid():
            product = Product.objects.get(id=ser.validated_data['id_of_product'])
            cart.add(product, quantity=ser.validated_data['quantity'])
            return Response({'massage': 'added'}, status=status.HTTP_201_CREATED)
        return Response(ser.errors)
class CartRemoveViewApi(APIView):
    serializer_class = CartRemoveAddOrderSerializer
    permission_classes = [IsAuthenticated,]
    def get(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.remove(product=product)
        return Response({'massage': 'deleted'}, status=status.HTTP_200_OK)
class AddOrderViewApi(APIView):
    serializer_class = CartRemoveAddOrderSerializer
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            for item in cart:
                product = Product.objects.get(id=ser.validated_data['id_of_product'])
                OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['quantity'])
                cart.clear()
                return Response({'massage': 'added order'},status=status.HTTP_201_CREATED)
            return Response({'error': 'have a problem in order'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



