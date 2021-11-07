from rest_framework import serializers


class Categoryerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    get_absolute_url = serializers.SerializerMethodField()


class ProductSerializer(serializers.Serializer):
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    # get_image = serializers.ImageField()
    # get_thumbnail = serializers.ImageField()
    # get_absolute_url = serializers.SerializerMethodField()




