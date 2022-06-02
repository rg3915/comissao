from django.urls import include, path

from backend.financial import views as v

app_name = 'financial'


comission_note_patterns = [
    path('', v.ComissionNoteListView.as_view(), name='comission_note_list'),  # noqa E501
    path('<int:pk>/', v.ComissionNoteDetailView.as_view(), name='comission_note_detail'),  # noqa E501
    path('create/', v.ComissionNoteCreateView.as_view(), name='comission_note_create'),  # noqa E501
    path('<int:pk>/update/', v.ComissionNoteUpdateView.as_view(), name='comission_note_update'),  # noqa E501
]

urlpatterns = [
    path('comission-note/', include(comission_note_patterns)),
]
