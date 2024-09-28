from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import (
    TailorCreationForm,
    OrderForm,
    TailorSearchForm,
    CustomerSearchForm,
    OrderSearchForm,
    ServiceSearchForm
)
from .models import (
    Order,
    Tailor,
    Service,
    Customer
)


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = ServiceSearchForm(
            initial={"model": name}
        )
        return context

    def get_queryset(self):
        form = ServiceSearchForm(self.request.GET)
        queryset = Service.objects.all()
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = CustomerSearchForm(
            initial={"model": last_name}
        )
        return context

    def get_queryset(self):
        form = CustomerSearchForm(self.request.GET)
        queryset = Customer.objects.all()
        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )
        return queryset


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
    order_list = Order.objects.filter(is_active=True).order_by('start_date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        short_description = self.request.GET.get("short_description", "")
        start_date = self.request.GET.get("start_date", "")
        finish_date = self.request.GET.get("finish_date", "")
        context["search_form"] = OrderSearchForm(
            initial={
                "short_description": short_description,
                "start_date": start_date,
                "finish_date": finish_date,
            }
        )
        return context

    def get_queryset(self):
        form = OrderSearchForm(self.request.GET)
        queryset = Order.objects.all()

        if form.is_valid():
            if form.cleaned_data["short_description"]:
                queryset = queryset.filter(
                    short_description__icontains=
                    form.cleaned_data["short_description"]
                )

            if form.cleaned_data["start_date"]:
                queryset = queryset.filter(
                    start_date__gte=
                    form.cleaned_data["start_date"]
                )

            if form.cleaned_data["finish_date"]:
                queryset = queryset.filter(
                    finish_date__lte=form.cleaned_data["finish_date"]
                )

        return queryset.order_by("-is_active", "start_date")


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    success_url = reverse_lazy("studio:order-list")
    template_name = "studio/order_form.html"
    form_class = OrderForm


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
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

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        if "assign" in request.POST:
            order.tailor = request.user
            order.save()
        elif "remove" in request.POST:
            if order.tailor == request.user:
                order.tailor = None
                order.save()
        return self.get(request, *args, **kwargs)


# crud for tailor
class TailorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tailor
    queryset = Tailor.objects.prefetch_related("orders")


class TailorListView(LoginRequiredMixin, generic.ListView):
    model = Tailor
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TailorListView, self).get_context_data(**kwargs)
        first_name = self.request.GET.get("first_name", "")
        context["search_form"] = TailorSearchForm(
            initial={"first_name": first_name}
        )
        return context

    def get_queryset(self):
        form = TailorSearchForm(self.request.GET)
        queryset = Tailor.objects.all()
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class TailorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tailor
    form_class = TailorCreationForm
    success_url = reverse_lazy("studio:tailor-list")


class TailorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tailor
    fields = "__all__"
    success_url = reverse_lazy("studio:tailor-list")


class TailorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tailor
    success_url = reverse_lazy("studio:tailor-list")
