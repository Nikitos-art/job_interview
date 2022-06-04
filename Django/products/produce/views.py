from django.http import HttpResponse
from django.shortcuts import render
from produce.models import Product, Category


def index(request):
    products = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'products': products,
        'cats': cats,
        'cat_selected': 0,
    }

    return render(request, 'goods_list.html', context=context)


def show_products(request, product_id):
    return HttpResponse(f"Отображение статьи с id = {product_id}")


def show_category(request, cat_id):
    prods = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'products': prods,
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'goods_list.html', context=context)
