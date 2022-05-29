from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.shortcuts import render


class BaseListView(ListView):
    queryset = Product.objects.all()
    template_name = 'base.html'


class ProductListViewAll(ListView):
    model = Product
    template_name = 'goods_list.html'

    def get_queryset(self):
        items = Product.objects.all()
        return items

# class ProductsListView(ListView):
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context.update({
#             'product': {
#                 "id": 3,
#                 "title": "potato",
#                 "description": "mini",
#                 "production_date": "2022-03-10",
#                 "price": 5,
#                 "measure_unit": "kg",
#                 "supplier_name": "local produce",
#             }
#         })
#         return context
