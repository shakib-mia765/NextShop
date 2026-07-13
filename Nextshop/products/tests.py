from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from .models import *

User = get_user_model()

# L19: Test Data Dictionary - Centralized test fixtures
TEST_DATA = {
    'USER': {'username': 'testuser', 'password': 'testpass123'},
    'CATEGORY': {'name': 'Electronics', 'slug': 'electronics'},
    'BRAND': {'name': 'Samsung'},
    'PRODUCT': {
        'name': 'Galaxy S24 Ultra',
        'price': Decimal('1299.99'),
        'discount_price': Decimal('1099.99'),
        'stock': 50,
        'currency': 'BDT',
        'status': 'published',
    },
    'VARIANT': {
        'variant_type': 'color',
        'value': 'Titanium Black',
        'price': Decimal('1299.99'),
        'stock': 20,
        'sku': 'GS24U-BLK-256',
    }
}

# L19: Expected Response Tuple - for assertion
PRODUCT_LIST_FIELDS = ('id', 'name', 'price', 'discount_price', 'stock', 'is_in_stock', 'discount_percent')

class ProductModelTest(TestCase):
    """L19: Model Layer Testing with Edge Cases"""
    
    def setUp(self):
        self.user = User.objects.create_user(**TEST_DATA['USER'])
        self.category = Category.objects.create(**TEST_DATA['CATEGORY'])
        self.brand = Brand.objects.create(**TEST_DATA['BRAND'])
        self.product_data = TEST_DATA['PRODUCT']
        self.product_data['category'] = self.category
        self.product_data['brand'] = self.brand
        self.product_data['seller'] = self.user
    
    def test_product_creation_and_slug(self):
        product = Product.objects.create(**self.product_data)
        self.assertEqual(product.slug, 'galaxy-s24-ultra')
        self.assertEqual(product.stock_status, 'in_stock')
    
    def test_stock_status_auto_update(self):
        product = Product.objects.create(**self.product_data)
        product.stock = 0
        product.save()
        self.assertEqual(product.stock_status, 'out_of_stock')
    
    def test_product_str_representation(self):
        product = Product.objects.create(**self.product_data)
        self.assertEqual(str(product), 'Galaxy S24 Ultra')

class ProductAPITest(APITestCase):
    """L19: API Layer Testing with Status Codes and Payload Validation"""
    
    def setUp(self):
        self.user = User.objects.create_user(**TEST_DATA['USER'])
        self.category = Category.objects.create(**TEST_DATA['CATEGORY'])
        self.brand = Brand.objects.create(**TEST_DATA['BRAND'])
        
        self.product = Product.objects.create(
            name=TEST_DATA['PRODUCT']['name'],
            price=TEST_DATA['PRODUCT']['price'],
            discount_price=TEST_DATA['PRODUCT']['discount_price
