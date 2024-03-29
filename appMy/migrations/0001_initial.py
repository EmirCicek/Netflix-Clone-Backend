# Generated by Django 5.0.1 on 2024-01-21 17:30

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
                ('title', models.CharField(max_length=50, verbose_name='Kategori')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Dizi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Dizi')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(max_length=250, upload_to='dizi', verbose_name='Dizi Resmi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
    ]
