from rest_framework import viewsets

from backend.crm.api.serializers import (
    CustomerSerializer,
    EmployeeCreateSerializer,
    EmployeeSerializer,
    EmployeeUpdateSerializer
)
from backend.crm.models import Customer, Employee


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeCreateSerializer

        if self.action == 'update' or self.action == 'partial_update':
            return EmployeeUpdateSerializer

        return EmployeeSerializer
