from django.urls import path
from .views import BaseListView, ProductListViewAll

# from .views import BaseListView, ProductListViewAll, add_data, product_add

urlpatterns = [
    path('', BaseListView.as_view(), name='main page'),
    path('goods_list', ProductListViewAll.as_view(), name='goods_list')
]

