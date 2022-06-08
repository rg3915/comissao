from rest_framework import serializers

from backend.crm.api.serializers import EmployeeSerializer
from backend.financial.models import ComissionNote, ComissionNoteItems
from backend.service.api.serializers import OrderItemsSerializer


class ComissionNoteItemsSerializer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer()

    class Meta:
        model = ComissionNoteItems
        fields = '__all__'


class ComissionNoteSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    comission_note_items = ComissionNoteItemsSerializer(
        source='comissionnoteitems_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = ComissionNote
        fields = '__all__'
