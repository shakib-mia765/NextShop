from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.StringRelatedField(many=True, read_only=True)
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'
    
    def get_product_count(self, obj):
        return obj.products.filter(status='published').count()

class BrandSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'
    def get_product_count(self, obj):
        return obj.products.count()

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True, allow_null=True)
    discount_percent = serializers.SerializerMethodField()
    is_in_stock = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug', 'stock_status', 'created_at', 'updated_at']
    
    def get_discount_percent(self, obj):
        if obj.discount_price and obj.price > 0:
            return round((obj.price - obj.discount_price) / obj.price * 100, 2)
        return 0
    
    def get_is_in_stock(self, obj):
        return obj.stock > 0
