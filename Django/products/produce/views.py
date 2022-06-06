from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from produce.models import Product, Category
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings


# class ProductListView(ListView):
#     model = Product
#     context_object_name = 'products'
#     template_name = 'goods_list.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context.update({
#             'site': get_current_site(request=self.request)
#         })
#         return context


# class CategoriesListView(ListView):
#     model = Category
#     context_object_name = 'cats'
#     template_name = 'goods_list.html'


def index(request):
    products = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'products': products,
        'cats': cats,
        'cat_selected': 0,
        'site': get_current_site(request=request)
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
        'site': get_current_site(request=request)
    }
    return render(request, 'goods_list.html', context=context)


