from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=40, verbose_name='Product Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='Preview', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    unit_price = models.IntegerField(verbose_name='Unit Price')
    creation_date = models.DateTimeField(verbose_name='Creation Date')
    last_modified = models.DateTimeField(verbose_name='Last Modified')

    def __str__(self):
        return f'Product Name: {self.product_name}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(models.Model):
    category_name = models.CharField(max_length=15, verbose_name='Category Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Creation Date', **NULLABLE)

    def __str__(self):
        return f'Category Name: {self.product_name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
