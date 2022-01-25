from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    get_image = serializers.CharField()
    get_thumbnail = serializers.CharField()
    get_absolute_url = serializers.CharField()


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    get_absolute_url = serializers.CharField()
    products = ProductSerializer(many=True)




