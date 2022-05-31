from django.shortcuts import render
from django.views.generic import ListView
from .models.product import Product
from django.shortcuts import render


class BaseListView(ListView):
    queryset = Product.objects.all()
    template_name = 'base.html'


class ProductListViewAll(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'goods_list.html'


def add_data(request):
    return render(request, 'goods_list.html', context={
        'object_list': Product.objects.all(),
        'product': {
            "title": "potato",
            "description": "mini",
            "production_date": "March 15, 2022",
            "price": 5,
            "measure_unit": "kg",
            "supplier_name": "local produce",
            "category": "food stuffs"
        }
    })

