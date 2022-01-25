from django.db.models import QuerySet, Q
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product, Category
from apps.products.serializers import ProductSerializer, CategorySerializer


class ProductApiViewSet(APIView):
    def get(self, request):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductDetail(APIView):
    def _get_objects(self, category_slug: str, product_slug: str) -> QuerySet:
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug: str, product_slug: str):
        product = self._get_objects(category_slug, product_slug)
        serializer = ProductSerializer(product)

        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        products = Product.objects.filter(category__slug=category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)


@api_view(['GET','POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    return Response({"products": []})
