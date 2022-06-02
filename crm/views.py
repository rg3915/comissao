from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from crm.models import Customer, Employee
from crm.serializers import CustomerSerializer, EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

