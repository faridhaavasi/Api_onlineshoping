from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

class CategoryListViewAPI(APIView):
    serializer_class = CategorySerializer
    def get(self, request):
        instance = Category.objects.all()
        serializer = CategorySerializer(instance=instance)
        return Response(serializer.data)






