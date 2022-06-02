from django.urls import include, path

from backend.crm import views as v

app_name = 'crm'


customer_patterns = [
    path('', v.CustomerListView.as_view(), name='customer_list'),  # noqa E501
    path('<int:pk>/', v.CustomerDetailView.as_view(), name='customer_detail'),  # noqa E501
    path('create/', v.CustomerCreateView.as_view(), name='customer_create'),  # noqa E501
    path('<int:pk>/update/', v.CustomerUpdateView.as_view(), name='customer_update'),  # noqa E501
]

employee_patterns = [
    path('', v.EmployeeListView.as_view(), name='employee_list'),  # noqa E501
    path('<int:pk>/', v.EmployeeDetailView.as_view(), name='employee_detail'),  # noqa E501
    path('create/', v.EmployeeCreateView.as_view(), name='employee_create'),  # noqa E501
    path('<int:pk>/update/', v.EmployeeUpdateView.as_view(), name='employee_update'),  # noqa E501
]


urlpatterns = [
    path('customer/', include(customer_patterns)),
    path('employee/', include(employee_patterns)),
]
