from rest_framework import serializers

from backend.crm.api.serializers import EmployeeSerializer
from backend.service.models import Order, OrderItems, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'description', 'price', 'comission')


class OrderItemsSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    service = ServiceSerializer()

    class Meta:
        model = OrderItems
        fields = '__all__'
        depth = 1


class OrderItemsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(
        source='orderitems_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
            'payment_type',
            'paid',
            'value',
            'created',
            'updated',
            'order_items',
        )
        depth = 1


class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = OrderItemsCreateSerializer(
        source='orderitems_set',
        many=True
    )

    class Meta:
        model = Order
        fields = (
            'customer',
            'payment_type',
            'paid',
            'value',
            'order_items',
        )


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
