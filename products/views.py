# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

# Internal:
from .models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def all_products(request):
    """
    View to show all products available in store

    Args:
        request (object): HTTP request object
    Returns:
        Render of products page
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search terms were entered!")
                return redirect(reverse('products'))

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)
