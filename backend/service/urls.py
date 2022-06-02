from django.urls import include, path

from backend.service import views as v

app_name = 'service'


service_patterns = [
    path('', v.ServiceListView.as_view(), name='service_list'),
    path('<int:pk>/', v.ServiceDetailView.as_view(), name='service_detail'),
    path('create/', v.ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/update/', v.ServiceUpdateView.as_view(), name='service_update'),
]

order_patterns = [
    path('', v.OrderListView.as_view(), name='order_list'),
    path('<int:pk>/', v.OrderDetailView.as_view(), name='order_detail'),
    path('create/', v.OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/update/', v.OrderUpdateView.as_view(), name='order_update'),
]


urlpatterns = [
    path('service/', include(service_patterns)),
    path('order/', include(order_patterns)),
]
