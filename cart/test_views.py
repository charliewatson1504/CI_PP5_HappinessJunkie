# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCartViews(TestCase):
    """
    Class for testing the cart views
    """

    def setUp(self):
        """
        Creates a test product
        """
        Product.objects.create(
            name='test_product',
            price='10',
            sku='HJ8001234567',
            description='This is a test product',
        )

    def tearDown(self):
        """
        Deletes the test product
        """
        Product.objects.all().delete()

    def test_view_cart_page(self):
        """
        Tests to check if cart page displays
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
