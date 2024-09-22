from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from studio.models import Service, Order, Customer

SERVICE_LIST_URL = reverse("studio:service-list")


class PublicServiceTest(TestCase):
    def test_login_required(self):
        """Тест перевіряє, що доступ до списку послуг вимагає авторизації"""
        response = self.client.get(SERVICE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f'/accounts/login/?next={SERVICE_LIST_URL}')


class PrivateServiceTest(TestCase):
    def setUp(self):
        """Налаштовуємо користувача для приватних тестів"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_service_list(self):
        """Тест перевіряє, що список послуг доступний авторизованому користувачу"""
        response = self.client.get(SERVICE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "studio/service_list.html")


class PrivateServiceDeleteTest(TestCase):
    def setUp(self):
        """Налаштовуємо користувача для приватних тестів"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_delete_service(self):
        """Тест перевіряє, що послуга може бути видалена авторизованим користувачем"""
        service = Service.objects.create(name="Test Service")
        delete_url = reverse("studio:service-delete", args=[service.id])
        response = self.client.post(delete_url)

        self.assertFalse(Service.objects.filter(id=service.id).exists())  # Перевіряємо, що послугу видалено
        success_url = reverse("studio:service-list")
        self.assertRedirects(response, success_url)

ORDER_LIST_URL = reverse("studio:order-list")


class PublicOrderTest(TestCase):
    def test_login_required(self):
        """Тест перевіряє, що доступ до списку замовлень вимагає авторизації"""
        response = self.client.get(ORDER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f'/accounts/login/?next={ORDER_LIST_URL}')


class PrivateOrderTest(TestCase):
    def setUp(self):
        """Налаштовуємо користувача для приватних тестів"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_order_list(self):
        """Тест перевіряє, що список замовлень доступний авторизованому користувачу"""
        response = self.client.get(ORDER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "studio/order_list.html")


class PrivateOrderDeleteTest(TestCase):
    def setUp(self):
        """Налаштовуємо користувача для приватних тестів"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_delete_order(self):
        """Тест перевіряє, що замовлення може бути видалено авторизованим користувачем"""
        customer = Customer.objects.create(first_name="John", last_name="Doe")
        order = Order.objects.create(short_description="Test Order", customer=customer)
        delete_url = reverse("studio:order-delete", args=[order.id])
        response = self.client.post(delete_url)

        self.assertFalse(Order.objects.filter(id=order.id).exists())  # Перевіряємо, що замовлення видалено
        success_url = reverse("studio:order-list")
        self.assertRedirects(response, success_url)

