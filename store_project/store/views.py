from django.shortcuts import render
from .models import Product, Customer, Order


def index(request):

    product_exact = Product.objects.filter(name__exact="iPhone")

    customers_contains = Customer.objects.filter(last_name__contains="dze")

    product_startswith = Product.objects.filter(name__startswith="Sam")

    product_endswith = Product.objects.filter(name__endswith="Pro")

    products_gt = Product.objects.filter(price__gt=100)

    products_gte = Product.objects.filter(price__gte=100)

    products_lt = Product.objects.filter(price__lt=50)

    products_lte = Product.objects.filter(price__lte=50)

    products_range = Product.objects.filter(price__range=(10, 50))

    products_in = Product.objects.filter(id__in=[1, 3, 5])

    customers_isnull = Customer.objects.filter(Email__isnull=True)

    context = {
        'product_exact': product_exact,
        'customers_contains': customers_contains,
        'product_startswith': product_startswith,
        'product_endswith': product_endswith,
        'products_gt': products_gt,
        'products_gte': products_gte,
        'products_lt': products_lt,
        'products_lte': products_lte,
        'products_range': products_range,
        'products_in': products_in,
        'customers_isnull': customers_isnull,
    }

    return render(request, 'index.html', context)
