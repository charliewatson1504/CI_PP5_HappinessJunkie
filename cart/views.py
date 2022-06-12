# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def view_cart(request):
    """
    View that renders the cart contents page

    Args:
        request (object): HTTP request object
    Returns:
        Renders cart page
    """
    return render(request, 'cart/cart.html')


def add_product_to_cart(request, item_id):
    """
    Adds product to the cart

    Args:
        request (object): HTTP request object
        item_id: Item ID
    Returns:
        redirect_url: Redirect to cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.friendly_name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(
            request, f'Added {product.friendly_name} to your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)
