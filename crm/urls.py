from django.urls import include, path
from rest_framework import routers

from crm.views import CustomerViewSet, EmployeeViewSet

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]