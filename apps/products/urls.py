from django.urls import path

from apps.products.views import (
    ProductApiViewSet,
    ProductDetail,
)

urlpatterns = [
    path('products-list/', ProductApiViewSet.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
]
