from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from suppliers.models import Contact, Product, Supplier


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )
    search_fields = (
        'email',
    )
    list_filter = (
        'country',
        'city',
    )


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model",
        "release_date",
    )
    search_fields = (
        'name',
        'model',
    )


@admin.register(Supplier)
class AdminSupplier(admin.ModelAdmin):
    list_select_related = True
    list_display = (
        "id",
        "name",
        "supplier_type",
        "contact",
        "contact__city",
        "provider_url",
        "debt_to_supplier",
        "creation_time",
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'supplier_type', "contact__city",
    )
    actions = ['knock_the_debts']

    @admin.action(description="Обнулить задолженность перед поставщиком")
    def knock_the_debts(self, queryset):
        queryset.update(debt=0)

    @admin.display(description="Поставщик")
    def provider_url(self, obj):
        if obj.provider:
            url = reverse('admin:suppliers_supplier_change', args=(obj.provider.id,))
            return format_html('<a href="%s">%s</a>' % (url, obj.provider.name), url)
        return None

    @admin.display(description="Город")
    def contact__city(self, obj):
        return obj.contact.city
