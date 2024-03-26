from rest_framework import serializers

from .models import Category, Product


class Sub_categorySerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)


class CategorySerializer(serializers.ModelSerializer):
    #sub_category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    sub_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_sub_category(self, obj):
        if obj.is_sub:
            serializer = Sub_categorySerializer(instance=obj.sub_category)
            return serializer.data

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image', 'available', 'price']
    def get_category(self, obj):
        if obj.category:
            serializer = CategorySerializer(instance=obj.category.all(), many=True)
            return serializer.data

