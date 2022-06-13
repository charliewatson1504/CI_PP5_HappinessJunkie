# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    zodiac_style = None
    if 'product_zodiac_style' in request.POST:
        zodiac_style = request.POST['product_zodiac_style']

    foil_print_color = None
    if 'product_foil_print_color' in request.POST:
        foil_print_color = request.POST['product_foil_print_color']

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            if zodiac_style:
                product = get_object_or_404(Product, pk-item_id)
                for zodiac_style, quantity in item_data['items_by_zodiac_style'].items():
                    total += quantity * product.price
                    product_count += quantity
                    cart.items.append({
                        'item_id': item_id,
                        'quantity': item_data,
                        'product': product,
                        'zodiac_style': zodiac_style,
                    })
            else:
                product = get_object_or_404(Product, pk-item_id)
                for foil_print_color, quantity in item_data['items_by_foil_print_color'].items():
                    total += quantity * product.price
                    product_count += quantity
                    cart.items.append({
                        'item_id': item_id,
                        'quantity': item_data,
                        'product': product,
                        'foil_print_color': foil_print_color,
                    })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
