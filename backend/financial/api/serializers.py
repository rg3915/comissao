from rest_framework import serializers

from backend.financial.models import ComissionNote, ComissionNoteItems


class ComissionNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionNote
        fields = '__all__'


class ComissionNoteItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionNoteItems
        fields = '__all__'
