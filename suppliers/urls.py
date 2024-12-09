from django.urls import path

from suppliers.views import ProductListAPIView, SupplierCreateAPIView, SupplierListAPIView, SupplierDetailAPIView, \
    SupplierUpdateAPIView, SupplierDeleteAPIView

app_name = "provider"

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="products_list"),
    path("suppliers/create/", SupplierCreateAPIView.as_view(), name="supplier_create"),
    path("suppliers/", SupplierListAPIView.as_view(), name="supplier_list"),
    path("suppliers/<int:pk>/", SupplierDetailAPIView.as_view(), name="supplier_detail"),
    path("suppliers/<int:pk>/update/", SupplierUpdateAPIView.as_view(), name="supplier_update"),
    path("suppliers/<int:pk>/delete/", SupplierDeleteAPIView.as_view(), name="supplier_delete"),
]
