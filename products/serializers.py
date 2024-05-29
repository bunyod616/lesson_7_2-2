from rest_framework import serializers
from .models import Category, Product


class CategoryGoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'