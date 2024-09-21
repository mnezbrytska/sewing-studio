from django.urls import path

from .views import (
    index,
    ServiceListView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    TailorListView,
    OrderListView,
    CustomerDetailView,
    OrderDetailView,
    TailorDetailView)

urlpatterns = [
    path("", index, name="index" ),
    path("services/", ServiceListView.as_view(), name="service-list"),
    path(
        "services/create/",
        ServiceCreateView.as_view(),
        name="service-create"),
    path(
        "services/<int:pk>/update/",
        ServiceUpdateView.as_view(),
        name="service-update"
    ),
    path(
        "services/<int:pk>/delete/",
        ServiceDeleteView.as_view(),
        name="service-delete"
    ),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
    path(
        "customers/create/",
        CustomerCreateView.as_view(),
        name="customer-create"
    ),
    path(
        "customers/<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customer-create"
    ),
    path("tailors/", TailorListView.as_view(), name="tailor-list"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path(
        "customers/<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path(
        "tailors/<int:pk>/",
        TailorDetailView.as_view(),
        name="tailor-detail"
    ),

]

app_name = "studio"

