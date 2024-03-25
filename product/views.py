from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .models import Category, Product

class CategoryListViewAPI(APIView):
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)



class ProductViewsetApi(viewsets.ViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        queryset = Product.objects.product_Avalible_True()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, slug):
        queryset = Product.objects.product_Avalible_True()
        product = get_object_or_404(queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)






