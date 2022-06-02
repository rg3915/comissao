from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from financial.models import ComissionNote, ComissionNoteItems
from financial.serializers import (ComissionNoteItemsSerializer,
                                   ComissionNoteSerializer)


class ComissionNoteViewSet(viewsets.ModelViewSet):
    queryset = ComissionNote.objects.all()
    serializer_class = ComissionNoteSerializer

class ComissionNoteItemsViewSet(viewsets.ModelViewSet):
    queryset = ComissionNoteItems.objects.all()
    serializer_class = ComissionNoteItemsSerializer

