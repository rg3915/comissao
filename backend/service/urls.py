from django.urls import include, path
from rest_framework import routers

from backend.service.api.viewsets import (
    OrderItemsViewSet,
    OrderViewSet,
    ServiceViewSet
)

app_name = 'service'

router = routers.DefaultRouter()

router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitem', OrderItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
