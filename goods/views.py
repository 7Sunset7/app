from django.shortcuts import render

from goods.models import Product


def catalog(requst):

    goods = Product.objects.all()
    context = {
        'title': 'Home - Каталог',
        'goods': goods
    }
    return render(requst, 'goods/catalog.html', context)


def product(requst):
    return render(requst, 'goods/product.html')
