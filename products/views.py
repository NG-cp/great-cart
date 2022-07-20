from django.shortcuts import get_object_or_404, render
<<<<<<< HEAD
from cart.models import CartItem

from category.models import Category
from .models import Products
from cart.views import _session_id

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
=======

from category.models import Category
from .models import Products
>>>>>>> aa6b27f (First Commit)

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
<<<<<<< HEAD
        pageinator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = pageinator.get_page(page)
        product_count = products.count()
    else:
        products = Products.objects.filter(is_available=True)
        pageinator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = pageinator.get_page(page)
=======
        product_count = products.count()
    else:
        products = Products.objects.filter(is_available=True)
>>>>>>> aa6b27f (First Commit)
        product_count = products.count()
    

    context = {
<<<<<<< HEAD
        'products': paged_products,
=======
        'products': products,
>>>>>>> aa6b27f (First Commit)
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
<<<<<<< HEAD
        is_product_in_cart = CartItem.objects.filter(cart__cart_id = _session_id(request), product=single_product).exists()
=======
>>>>>>> aa6b27f (First Commit)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
<<<<<<< HEAD
        'is_product_in_cart': is_product_in_cart,
    }

    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Products.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
=======
    }

    return render(request, 'store/product_detail.html', context)
>>>>>>> aa6b27f (First Commit)
