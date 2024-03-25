from rest_framework import serializers
from .models import Category, Product
from rest_framework.response import Response

class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Category
        fields = ('name','sub_category')

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image', 'available', 'price']
    def get_category(self, obj):
        print(30*'.')
        print(obj.category)
