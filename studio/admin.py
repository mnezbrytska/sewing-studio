from django.contrib import  admin
from django.contrib.auth.admin import UserAdmin

from studio.models import Service, Order, Tailor, Customer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer", "tailor", "start_date", "finish_date", "is_urgent",
        "display_services", "is_active", "is_paid"
                    )
    list_filter = (
        "customer__last_name", "tailor__username",
        "start_date", "finish_date", "is_active"
    )
    search_fields = ("customer__last_name", "short_description")

    def display_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])
    display_services.short_description = "Services"


admin.site.register(Service)
admin.site.register(Tailor, UserAdmin)
admin.site.register(Customer)
