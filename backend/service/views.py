from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import OrderForm, ServiceForm
from .models import Order, Service


class ServiceListView(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm


class OrderListView(ListView):
    model = Order


class OrderDetailView(DetailView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
