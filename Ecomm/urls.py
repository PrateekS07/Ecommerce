from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products.views import ProductList, ProductDetail
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
]
