from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ComissionNoteForm
from .models import ComissionNote


class ComissionNoteListView(ListView):
    model = ComissionNote


class ComissionNoteDetailView(DetailView):
    model = ComissionNote


class ComissionNoteCreateView(CreateView):
    model = ComissionNote
    form_class = ComissionNoteForm


class ComissionNoteUpdateView(UpdateView):
    model = ComissionNote
    form_class = ComissionNoteForm
