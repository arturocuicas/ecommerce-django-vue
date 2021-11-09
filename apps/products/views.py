from django.db.models import QuerySet
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductApiViewSet(APIView):
    def get(self, request):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDetail(APIView):
    @staticmethod
    def _get_objects(category_slug: str, product_slug: str) -> QuerySet:
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug: str, product_slug: str):
        product = self._get_objects(category_slug, product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)
