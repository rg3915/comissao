from django.urls import include, path
from rest_framework import routers

from financial.views import ComissionNoteItemsViewSet, ComissionNoteViewSet

router = routers.DefaultRouter()

router.register(r'comissionnotes', ComissionNoteViewSet)
router.register(r'comissionnoteitem', ComissionNoteItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]