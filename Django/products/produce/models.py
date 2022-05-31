from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название товара')
    description = models.CharField(max_length=256, verbose_name='Описание')
    production_date = models.DateField(verbose_name='Дата производства')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    measure_unit = models.CharField(max_length=32, verbose_name='Единица измерения')
    supplier_name = models.CharField(max_length=64, verbose_name='Имя поставщика')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="Consumer products")



