from rest_framework import viewsets

from backend.service.api.serializers import (
    OrderItemsSerializer,
    OrderSerializer,
    ServiceSerializer
)
from backend.service.models import Order, OrderItems, Service


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
