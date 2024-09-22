from django.test import TestCase
from django.contrib.auth import get_user_model

from studio.forms import TailorSearchForm, OrderSearchForm, ServiceSearchForm, CustomerSearchForm
from studio.models import Tailor, Order, Service, Customer


class TailorSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.tailor = get_user_model().objects.create_user(
            username="test_tailor",
            password="testpassword",
            first_name="John",
            last_name="Doe"
        )

    def test_tailor_search_form_valid_data(self) -> None:
        form_data = {"username": "test_tailor"}
        form = TailorSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        tailors = Tailor.objects.filter(
            username__icontains=form_data["username"]
        )
        self.assertEqual(list(tailors), [self.tailor])


class OrderSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="123456789"
        )
        self.order = Order.objects.create(
            short_description="Urgent tailoring",
            customer=self.customer,
            start_date="2024-09-01",
            finish_date="2024-09-10",
            is_urgent=True,
        )

    def test_order_search_form_valid_data(self) -> None:
        form_data = {"short_description": "Urgent tailoring"}
        form = OrderSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        orders = Order.objects.filter(
            short_description__icontains=form_data["short_description"]
        )
        self.assertEqual(list(orders), [self.order])


class ServiceSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.service = Service.objects.create(
            name="Tailoring",
            price=100.00
        )

    def test_service_search_form_valid_data(self) -> None:
        form_data = {"name": "Tailoring"}
        form = ServiceSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        services = Service.objects.filter(
            name__icontains=form_data["name"]
        )
        self.assertEqual(list(services), [self.service])


class CustomerSearchFormTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="123456789"
        )

    def test_customer_search_form_valid_data(self) -> None:
        form_data = {"last_name": "Doe"}
        form = CustomerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        customers = Customer.objects.filter(
            last_name__icontains=form_data["last_name"]
        )
        self.assertEqual(list(customers), [self.customer])
