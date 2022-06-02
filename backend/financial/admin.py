from django.contrib import admin

from .models import ComissionNote, ComissionNoteItems


@admin.register(ComissionNote)
class ComissionNoteAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(ComissionNoteItems)
class ComissionNoteItemsAdmin(admin.ModelAdmin):
    exclude = ()
