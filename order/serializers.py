from rest_framework import serializers


class CartAddSerializer(serializers.Serializer):
    id_of_product = serializers.IntegerField()
    quantity = serializers.IntegerField()