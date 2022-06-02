from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from produce.models import Product, Category
from django.shortcuts import render


class BaseListView(ListView):
    queryset = Product.objects.all()
    template_name = 'base.html'


class ProductListViewAll(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'goods_list.html'




