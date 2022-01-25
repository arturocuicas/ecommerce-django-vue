from django.urls import path

from apps.products.views import (
    ProductApiViewSet,
    ProductDetail,
    CategoryDetail,
    search,
)

urlpatterns = [
    path('products-list/', ProductApiViewSet.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]
