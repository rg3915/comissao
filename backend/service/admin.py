from django.contrib import admin

from .models import Order, OrderItems, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    exclude = ()


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline,)
    exclude = ()


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    exclude = ()
