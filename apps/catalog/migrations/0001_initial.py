# Generated by Django 4.2.1 on 2023-05-27 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=15, verbose_name='Category Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Preview')),
                ('unit_price', models.IntegerField(verbose_name='Unit Price')),
                ('creation_date', models.DateTimeField(verbose_name='Creation Date')),
                ('last_modified', models.DateTimeField(verbose_name='Last Modified')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]