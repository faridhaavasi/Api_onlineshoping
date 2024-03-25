from rest_framework import serializers
from unicodedata import name

from .models import Category, Product
from rest_framework.response import Response

class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Category
        fields = ('name','sub_category')

    #

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image', 'available', 'price']
    def get_category(self, obj):
        if obj.category:
            serializer = CategorySerializer(instance=obj.category.all(), many=True)
            return serializer.data

