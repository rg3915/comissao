from django.urls import include, path
from rest_framework import routers

from backend.crm.api.viewsets import CustomerViewSet, EmployeeViewSet

app_name = 'crm'

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
