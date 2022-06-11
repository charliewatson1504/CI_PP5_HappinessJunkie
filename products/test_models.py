# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase


# Internal:
from .models import Category, Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductModels(TestCase):
    """
    Class to test product models
    """

    def setUp(self):
        """
        This creates a test product and category
        """

        Category.objects.create(
            name='test_category',
            friendly_name='Test Category')

        Product.objects.create(
            name='test_product',
            friendly_name='Test Product',
            price='10',
            sku='hj8001234567',
            description='This is a test description',
            has_sticker_finish=True,
        )

    def tearDown(self):
        """
        This deletes the test product and category
        """
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_category_str_method(self):
        """
        Tests the str method of categories
        """
        category = Category.objects.get(name='test_category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_product_str_method(self):
        """
        Tests the str method of product
        """
        product = Product.objects.get(sku='hj8001234567')
        self.assertEqual((product.__str__()), product.name)
