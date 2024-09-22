from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TailorCreationForm, OrderForm
from .models import Order, Tailor, Service, Customer


@login_required
def index(request):
    """View function for the home page of the site."""
    num_tailors = Tailor.objects.count()
    num_orders = Order.objects.count()
    num_customers = Customer.objects.count()
    num_services = Service.objects.count()
    num_visits = request.session.get("num_visit", 0)
    request.session["num_visit"] = num_visits + 1
    context = {
        "num_tailors": num_tailors,
        "num_orders": num_orders,
        "num_customers": num_customers,
        "num_services": num_services,
        "num_visits": num_visits + 1
    }
    return render(request, "studio/index.html", context=context)


# crud for services
class ServiceListView(LoginRequiredMixin, generic.ListView):
    model = Service
    paginate_by = 10


class ServiceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Service
    fields = "__all__"
    success_url = reverse_lazy("studio:service-list")
    template_name = "studio/service_form.html"


class ServiceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Service
    fields = "__all__"
    success_url = reverse_lazy("studio:service-list")
    template_name = "studio/service_form.html"


class ServiceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Service
    fields = "__all__"
    success_url = reverse_lazy("studio:service-list")
    template_name = "studio/service_delete.html"


# crud for customers
class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    queryset = Customer.objects.order_by("last_name")
    paginate_by = 10


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("studio:customer-list")
    template_name = "studio/customer_form.html"


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("studio:customer-list")
    template_name = "studio/customer_form.html"


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("studio:customer-list")
    template_name = "studio/customer_delete.html"


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    queryset = Customer.objects.prefetch_related("orders")


# crud for orders
class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    paginate_by = 10


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    # fields = "__all__"
    success_url = reverse_lazy("studio:order-list")
    template_name = "studio/order_form.html"
    form_class = OrderForm


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    # fields = "__all__"
    success_url = reverse_lazy("studio:order-list")
    template_name = "studio/order_form.html"
    form_class = OrderForm


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    fields = "__all__"
    success_url = reverse_lazy("studio:order-list")
    template_name = "studio/order_delete.html"


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    queryset = Order.objects.select_related(
        "customer").prefetch_related("services")


# crud for tailor
class TailorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tailor
    queryset = Tailor.objects.prefetch_related("orders")


class TailorListView(LoginRequiredMixin, generic.ListView):
    model = Tailor


class TailorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tailor
    form_class = TailorCreationForm
    success_url = reverse_lazy("studio:tailor-list")


class TailorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tailor
    fields = "__all__"
    # form_class = TailorLicenseUpdateForm
    success_url = reverse_lazy("studio:tailor-list")


class TailorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tailor
    success_url = reverse_lazy("studio:tailor-list")