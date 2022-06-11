from django.urls import path
from .views import index, show_category, show_products

urlpatterns = [
    path('', index, name='home'),
    # path('product/', ProductListView.as_view(), name='product'),
    # path('category/', CategoriesListView.as_view(), name='category'),

    path('product/<int:product_id>/', show_products, name='product'),
    path('category/<int:cat_id>/', show_category, name='category'),
]

