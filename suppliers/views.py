from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from suppliers.filters import SupplierFilter
from suppliers.models import Product, Supplier
from suppliers.paginators import CustomPagination
from suppliers.serializers import ProductSerializer, SupplierSerializer, SupplierUpdateSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_class = SupplierFilter
    filter_backends = (DjangoFilterBackend,)


class SupplierDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SupplierUpdateSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]


class SupplierDeleteAPIView(generics.DestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated]
