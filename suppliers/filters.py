import django_filters

from suppliers.models import Supplier


class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(field_name='contact__country', lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = []
