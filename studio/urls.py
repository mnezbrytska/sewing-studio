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
    CustomerDeleteView,
    CustomerDetailView,

    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    OrderDetailView,

    TailorDetailView,
    TailorListView,
    TailorCreateView,
    TailorUpdateView,
    TailorDeleteView,
)

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
        name="customer-update"
    ),
    path(
        "customers/<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete"
    ),
    path(
        "customers/<int:pk>/",
        CustomerDetailView.as_view(),
        name="customer-detail"
    ),

    path("orders/", OrderListView.as_view(), name="order-list"),
    path(
        "orders/create/",
        OrderCreateView.as_view(),
        name="order-create"
    ),
    path(
        "orders/<int:pk>/update/",
        OrderUpdateView.as_view(),
        name="order-update"
    ),
    path(
        "orders/<int:pk>/delete/",
        OrderDeleteView.as_view(),
        name="order-delete"
    ),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path(
        "tailors/<int:pk>/",
        TailorDetailView.as_view(),
        name="tailor-detail"
    ),
    path("tailors/", TailorListView.as_view(), name="tailor-list"),
    path(
        "tailors/create/", TailorCreateView.as_view(), name="tailor-create"
    ),
    path(
        "tailors/<int:pk>/update/",
        TailorUpdateView.as_view(),
        name="tailor-update"
    ),

    path(
        "tailors/<int:pk>/delete/",
        TailorDeleteView.as_view(),
        name="tailor-confirm-delete"
    ),

]

app_name = "studio"

