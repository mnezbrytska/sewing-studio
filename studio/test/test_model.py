from django.test import TestCase
from studio.models import Customer, Service, Tailor, Order
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import date

class ModelTests(TestCase):

    def test_customer_str(self):
        """Тест для методу __str__ моделі Customer"""
        customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="123456789",
            email="john.doe@example.com"
        )
        self.assertEqual(str(customer), "Doe John")

    def test_service_str(self):
        """Тест для методу __str__ моделі Service"""
        service = Service.objects.create(
            name="Tailoring",
            price=100.00
        )
        self.assertEqual(str(service), "Tailoring")

    def test_tailor_str(self):
        """Тест для методу __str__ моделі Tailor"""
        tailor = get_user_model().objects.create_user(
            username="tailor1",
            first_name="Jane",
            last_name="Smith",
            password="password123"
        )
        self.assertEqual(str(tailor), "tailor1 (Jane Smith)")


    def test_calculate_total_price(self):
        """Тест для методу calculate_total_price моделі Order"""
        service1 = Service.objects.create(name="Tailoring", price=50.00)
        service2 = Service.objects.create(name="Repair", price=30.00)
        customer = Customer.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="123456789",
            email="john.doe@example.com"
        )
        order = Order.objects.create(
            start_date=date.today(),
            finish_date=date.today(),
            short_description="Urgent tailoring",
            customer=customer,
            is_urgent=True,
            is_active=True
        )
        order.services.add(service1, service2)
        self.assertEqual(order.calculate_total_price(), 80.00)
