from rest_framework import serializers


class CartSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    unit_price = serializers.IntegerField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)

