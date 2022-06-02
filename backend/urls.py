from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('', include('backend.crm.urls', namespace='crm')),
    path('', include('backend.financial.urls', namespace='financial')),
    path('', include('backend.service.urls', namespace='service')),
    path('admin/', admin.site.urls),
]
