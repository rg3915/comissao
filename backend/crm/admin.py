from django.contrib import admin

from .models import Customer, Employee


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    exclude = ()
