from django.urls import include, path

from backend.service import views as v

app_name = 'service'


service_patterns = [
    path('', v.ServiceListView.as_view(), name='service_list'),  # noqa E501
    path('<int:pk>/', v.ServiceDetailView.as_view(), name='service_detail'),  # noqa E501
    path('create/', v.ServiceCreateView.as_view(), name='service_create'),  # noqa E501
    path('<int:pk>/update/', v.ServiceUpdateView.as_view(), name='service_update'),  # noqa E501
]

order_patterns = [
    path('', v.OrderListView.as_view(), name='order_list'),  # noqa E501
    path('<int:pk>/', v.OrderDetailView.as_view(), name='order_detail'),  # noqa E501
    path('create/', v.OrderCreateView.as_view(), name='order_create'),  # noqa E501
    path('<int:pk>/update/', v.OrderUpdateView.as_view(), name='order_update'),  # noqa E501
]


urlpatterns = [
    path('service/', include(service_patterns)),
    path('order/', include(order_patterns)),
]
