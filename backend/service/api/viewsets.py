from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.financial.models import ComissionNote, ComissionNoteItems
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

    @action(detail=True, methods=['post'])
    def generate_comission_note(self, request, pk=None):
        '''
        Gera Notas de Comissão para cada Funcionário a partir do Pedido selecionado.
        '''
        order = self.get_object()
        order_items = order.orderitems_set.all()
        comission_note_items = ComissionNoteItems.objects.values_list(
            'order_items', flat=True)

        for item in order_items:
            if item.pk not in comission_note_items:
                cn = ComissionNote.objects.filter(
                    employee=item.employee, paid=False).first()
                if cn:
                    ComissionNoteItems.objects.create(
                        comission_note=cn,
                        order_items=item,
                        quantity=item.quantity,
                        comission=item.price * item.comission_employee
                    )
                else:
                    # Cria as Notas de Comissão.
                    comission_note = ComissionNote.objects.create(
                        employee=item.employee,
                        created_by=User.objects.first()
                    )

                    ComissionNoteItems.objects.create(
                        comission_note=comission_note,
                        order_items=item,
                        quantity=item.quantity,
                        comission=item.price * item.comission_employee
                    )

        return Response({})


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
