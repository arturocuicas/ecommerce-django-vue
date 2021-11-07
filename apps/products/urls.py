from django.urls import path

from apps.products.views import (
    ProductApiViewSet
)

urlpatterns = [
    path('products/', ProductApiViewSet.as_view()),
]
