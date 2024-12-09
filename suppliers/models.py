import django
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    email = models.EmailField(unique=True, blank=True, null=True, verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.PositiveIntegerField(verbose_name='номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    SUPPLIER_CHOICES = [
        ('З', 'Завод'),
        ('РС', 'Розничная сеть'),
        ('ИП', 'Индивидуальный предприниматель'),
        ]
    name = models.CharField(max_length=100, verbose_name='название поставщика')
    supplier_type = models.CharField(max_length=35, choices=SUPPLIER_CHOICES, verbose_name='тип поставщика')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='контакт', primary_key=False)
    product = models.ManyToManyField(Product, verbose_name='продукты', blank=True)
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', blank=True, null=True)
    debt_to_supplier = models.FloatField(default=0, verbose_name='долг перед поставщиком')
    creation_time = models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания')
