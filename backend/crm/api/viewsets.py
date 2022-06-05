from rest_framework import viewsets

from backend.crm.api.serializers import CustomerSerializer, EmployeeSerializer
from backend.crm.models import Customer, Employee


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
