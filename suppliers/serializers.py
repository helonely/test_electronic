from rest_framework import serializers
from rest_framework.fields import CharField

from suppliers.models import Contact, Product, Supplier


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(Contact.objects.all())

    class Meta:
        model = Supplier
        fields = ("name", "contact")


class SupplierSerializer(serializers.ModelSerializer):
    product_queryset = Product.objects.all()
    product = ProductSerializer(product_queryset, many=True)
    contact_data = Contact.objects.all()
    contact = ContactSerializer(contact_data)
    supplier = ProviderSerializer()

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    debt = CharField(read_only=True)

    class Meta:
        model = Supplier
        fields = "__all__"
