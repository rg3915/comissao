from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CustomerForm, EmployeeForm
from .models import Customer, Employee


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm


class EmployeeListView(ListView):
    model = Employee


class EmployeeDetailView(DetailView):
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
