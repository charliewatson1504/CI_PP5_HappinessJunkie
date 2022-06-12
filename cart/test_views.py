# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages

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

    def test_add_item_to_cart_no_variation(self):
        """
        Test adding a product to the cart that has no variations
        """
        product = Product.objects.get(sku='HJ8001234567')
        response = self.client.post(
            f'/cart/add/{product.id}/', {"quantity": 1, "redirect_url": "view_cart"})
        cart = self.client.session['cart']
        self.assertEqual(car[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added to your cart!')
