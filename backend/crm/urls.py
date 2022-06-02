from django.urls import include, path

from backend.crm import views as v

app_name = 'crm'


customer_patterns = [
    path('', v.CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', v.CustomerDetailView.as_view(), name='customer_detail'),
    path('create/', v.CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/update/', v.CustomerUpdateView.as_view(), name='customer_update'),
]

employee_patterns = [
    path('', v.EmployeeListView.as_view(), name='employee_list'),
    path('<int:pk>/', v.EmployeeDetailView.as_view(), name='employee_detail'),
    path('create/', v.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/update/', v.EmployeeUpdateView.as_view(), name='employee_update'),
]


urlpatterns = [
    path('customer/', include(customer_patterns)),
    path('employee/', include(employee_patterns)),
]
