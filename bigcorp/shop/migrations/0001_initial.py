# Generated by Django 5.0.6 on 2024-05-19 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('brand', models.CharField(max_length=245, verbose_name='Бренд')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=255, verbose_name='Слаг')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='product/products/%Y/%m/%d', verbose_name='Изображение')),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('shop.product',),
        ),
    ]
