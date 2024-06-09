from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=50, unique=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
        ordering = ['id']


class Store(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True)
    products = models.ManyToManyField(Product, related_name='stores')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = 'Магазины'
        ordering = ['id']