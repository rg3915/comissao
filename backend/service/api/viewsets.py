from rest_framework import viewsets

from backend.service.api.serializers import (
    OrderCreateSerializer,
    OrderItemsSerializer,
    OrderSerializer,
    OrderUpdateSerializer,
    ServiceSerializer
)
from backend.service.models import Order, OrderItems, Service


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer

        if self.action == 'update' or self.action == 'partial_update':
            return OrderUpdateSerializer

        return OrderSerializer

    def perform_create(self, serializer):
        # Pega os Itens do Pedido.
        order_items = serializer.validated_data.pop('orderitems_set')
        # Salva o Pedido
        order = serializer.save()

        # Salva os Itens do Pedido.
        for item in order_items:
            OrderItems.objects.create(**item, order=order)


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
