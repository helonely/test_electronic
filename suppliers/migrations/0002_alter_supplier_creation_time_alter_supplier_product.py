# Generated by Django 5.1.3 on 2024-12-09 19:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='product',
            field=models.ManyToManyField(blank=True, to='suppliers.product', verbose_name='продукты'),
        ),
    ]
