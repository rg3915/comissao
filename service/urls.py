from django.urls import include, path
from rest_framework import routers

from service.views import OrderItemsViewSet, OrderViewSet, ServiceViewSet

router = routers.DefaultRouter()

router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitem', OrderItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]