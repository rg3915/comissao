from django.contrib import admin

from .models import Order, OrderItems, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price', 'comission')
    search_fields = ('description',)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline,)
    list_display = ('__str__', 'customer', 'payment_type', 'paid', 'value')
    search_fields = ('name',)
    list_filter = ('paid', 'payment_type',)
    date_hierarchy = 'created'
    ordering = ('-created',)


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    exclude = ()
