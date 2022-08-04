# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.urls import reverse

# Internal:
from .models import Category, Product, Review
from .forms import ProductForm, ProductReviewForm
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
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search terms were entered!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:

            # not use currently as categories not split but available for
            # future store enhancements
            categories = request.GET['category'].split(',')

            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def average_star_rating(reviews):
    rounded_average = 0
    number_of_reviews = 0
    sum_of_star_ratings = 0

    for review in reviews:
        number_of_reviews = number_of_reviews + 1
        sum_of_star_ratings = sum_of_star_ratings + review.star_rating

    if number_of_reviews > 0:
        average = (sum_of_star_ratings / number_of_reviews)
        rounded_average = int(round(average, 1))
        return rounded_average
    else:
        return rounded_average


def product_detail(request, product_id):
    """
    View to show product detail page for selected product

    Args:
        request (object): HTTP request object
        product_id: Product ID
    Returns:
        Render of the product detail page
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product).order_by('-created_on')
    number_of_reviews = reviews.count()
    review_form = ProductReviewForm(data=request.POST or None)
    rounded_average = average_star_rating(reviews)

    Product.objects.filter(id=product.id).update(star_rating=rounded_average)

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
        'number_of_reviews': number_of_reviews,
        'rounded_average': rounded_average,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Adds a product to the site

    Args:
        request (object): HTTP request object
    Returns:
        Render of add product page
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies but only store owner accounts can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, 'You have successfully created a new product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Product creation failed. Please check form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Allows a superuser to edit a product

    Args:
        request (object): HTTP request object
        product_id: Product ID
    Returns:
        Render of edit product page
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies but only store owner accounts can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated the product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Product update failed. Please check form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are updating {product.friendly_name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Deletes a product from site

    Args:
        request (object): HTTP request object
        product_id: Product ID
    Returns:
        Redirect to products page
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies but only store owner accounts can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been successfully removed!')

    return redirect(reverse('products'))


@login_required
def add_a_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_review_form = ProductReviewForm(request.POST)

        if product_review_form.is_valid():
            is_product_reviewed = Review.objects.filter(product=product,
                                                        user=request.user)
            if not is_product_reviewed:
                Review.objects.create(
                    user=request.user,
                    product=product,
                    star_rating=request.POST['star_rating'],
                    review_text=request.POST['review_text'],
                    is_recommended=request.POST['is_recommended']
                )
            else:
                messages.error(
                    request,
                    f'{request.user}, you have already left a review for this product.'
                )

            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Something went wrong, failed to a review')
    messages.error(request, 'Something went wrong, invalid method')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_a_review(request, product_id, review_id):
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.user.is_superuser:

        if request.method == 'POST':
            review.delete()
            messages.info(request, 'Review has been deleted successfully')
        else:
            messages.error(request, 'Error deleting review, please try again')
    else:
        messages.error(request,
                       f'{request.user} - only store owners are able to remove reviews.')
        return redirect(reverse('home'))
    return redirect(reverse('product_detail', args=[product.id]))
