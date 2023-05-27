from django.db import models

class Product(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

class Category(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
