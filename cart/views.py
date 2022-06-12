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

    zodiac_style = None
    if 'product_zodiac_style' in request.POST:
        zodiac_style = request.POST['product_zodiac_style']

    foil_print_color = None
    if 'product_foil_print_color' in request.POST:
        foil_print_color = request.POST['product_foil_print_color']

    cart = request.session.get('cart', {})

    if zodiac_style:
        if item_id in list(cart.keys()):
            if zodiac_style in cart[item_id]['item_by_zodiac_style'].keys():
                cart[item_id]['item_by_zodiac_style'] += quantity
                messages.success(
                    request,
                    f'Updated {zodiac_style} {product.friendly_name} quantity to {cart[item_id]["item_by_zodiac_style"][zodiac_style]}')
            else:
                cart[item_id]['item_by_zodiac_style'][zodiac_style] = quantity
                messages.success(
                    request, f'Added {zodiac_style} {product.friendly_name} to your cart')
        else:
            cart[item_id] = {'item_by_zodiac_style': {zodiac_style: quantity}}
            messages.success(
                request, f'Added {zodiac_style} {product.friendly_name} to your cart')
    elif foil_print_color:
        if item_id in list(cart.keys()):
            if foil_print_color in cart[item_id]['item_by_foil_print_color'].keys():
                cart[item_id]['item_by_foil_print_color'] += quantity
                messages.success(
                    request,
                    f'Updated {foil_print_color} {product.friendly_name} quantity to {cart[item_id]["item_by_foil_print_color"][foil_print_color]}')
            else:
                cart[item_id]['item_by_foil_print_color'][foil_print_color] = quantity
                messages.success(
                    request, f'Added {foil_print_color} {product.friendly_name} to your cart')
        else:
            cart[item_id] = {'item_by_foil_print_color': {
                foil_print_color: quantity}}
            messages.success(
                request, f'Added {foil_print_color} {product.friendly_name} to your cart')
    else:
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
