from django.urls import path
from .views import ListCreateProductAPIView, RetrieveUpdateDestroyProductAPIView, ListCreateCategoryAPIView, RetrieveUpdateDestroyCategoryAPIView

urlpatterns = [
    path('categories/', ListCreateCategoryAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', RetrieveUpdateDestroyCategoryAPIView.as_view(), name='category-detail'),
    path('product/', ListCreateProductAPIView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', RetrieveUpdateDestroyProductAPIView.as_view(), name='product-detail'),
]

