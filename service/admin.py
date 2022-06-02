from django.contrib import admin

from service.models import Order, OrderItems, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    exclude = ()
