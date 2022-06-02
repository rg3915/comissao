from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from service.models import Order, OrderItems, Service
from service.serializers import (OrderItemsSerializer, OrderSerializer,
                                 ServiceSerializer)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

