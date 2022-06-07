from django.urls import include, path
from rest_framework import routers

from backend.financial.api.viewsets import (
    ComissionNoteItemsViewSet,
    ComissionNoteViewSet
)

app_name = 'financial'

router = routers.DefaultRouter()

router.register(r'comissionnotes', ComissionNoteViewSet)
router.register(r'comissionnoteitem', ComissionNoteItemsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
