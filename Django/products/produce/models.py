from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название товара')
    description = models.CharField(max_length=256, verbose_name='Описание')
    production_date = models.DateField(verbose_name='Дата производства')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    measure_unit = models.CharField(max_length=32, verbose_name='Единица измерения')
    supplier_name = models.CharField(max_length=64, verbose_name='Имя поставщика')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=32)
    site = models.OneToOneField(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
