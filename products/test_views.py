# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from .models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductViews(TestCase):
    """
    Class for testing the product views
    """

    def setUp(self):
        """
        This creates a test product
        """
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
        This deletes the test product
        """

    def test_get_all_products(self):
        """
        Tests getting the all products page
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_search_empty_query(self):
        """
        Tests searching without entering a query
        """
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')

    def test_product_search(self):
        """
        Test seraching for a product
        """
        response = self.client.get('/products/', {'q': 'test product'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
