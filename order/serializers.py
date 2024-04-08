from rest_framework import serializers


class CartAddSerializer(serializers.Serializer):
    id_of_product = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField(write_only=True)


class CartRemoveAddOrderSerializer(serializers.Serializer):
    id_of_product = serializers.IntegerField(write_only=True)






