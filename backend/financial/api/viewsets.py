from rest_framework import viewsets

from backend.financial.api.serializers import (
    ComissionNoteItemsSerializer,
    ComissionNoteSerializer
)
from backend.financial.models import ComissionNote, ComissionNoteItems


class ComissionNoteViewSet(viewsets.ModelViewSet):
    queryset = ComissionNote.objects.all()
    serializer_class = ComissionNoteSerializer


class ComissionNoteItemsViewSet(viewsets.ModelViewSet):
    queryset = ComissionNoteItems.objects.all()
    serializer_class = ComissionNoteItemsSerializer
