from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v100', include('djoser.urls')),
    path('api/v100', include('djoser.urls.authtoken')),
]
