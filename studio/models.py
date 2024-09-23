from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ("last_name", )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Service(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name


class Tailor(AbstractUser):

    class Meta:
        verbose_name = "Tailor"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("studio:tailor-detail", kwargs={"pk": self.pk})


class Order(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    short_description = models.CharField(max_length=250)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    tailor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )
    is_urgent = models.BooleanField(default=False)
    services = models.ManyToManyField(Service, related_name="orders")
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-is_active", "start_date")

    def __str__(self):
        return f"{self.customer} {self.services} {self.short_description} "


    def calculate_total_price(self):
        return sum(service.price for service in self.services.all())
