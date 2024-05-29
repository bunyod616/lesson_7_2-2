from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryProductSerializers, ProductSerializers
from .models import Category, Product
from rest_framework.views import APIView
# Create your views here.

class ListCreateCategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryProductSerializers(categories, many=True)
        return Response({'category': serializer.data, 'status': "success"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyCategoryAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryProductSerializers(category)
        return Response({'category': serializer.data, 'status': 'success'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryProductSerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'update'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_200_OK)
        serializer = CategoryProductSerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'category': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'status': 'delete'}, status=status.HTTP_204_NO_CONTENT)


class ListCreateProductAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response({'product': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': serializer.data, 'status': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDestroyProductAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializers(product)
        return Response({'product': serializer.data, 'status': 'success'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'poduct': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': serializer.data, 'status': 'updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({'error': 'Товар не найден'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)







