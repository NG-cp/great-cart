from multiprocessing import context
from django.shortcuts import render
from products.models import Products, ReviewRating

def home(request):
    products = Products.objects.all().filter(is_available=True).order_by('created_date')

    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)