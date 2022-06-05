from django.contrib import admin

from .models import ComissionNote, ComissionNoteItems


class ComissionNoteItemsInline(admin.TabularInline):
    model = ComissionNoteItems
    extra = 0


@admin.register(ComissionNote)
class ComissionNoteAdmin(admin.ModelAdmin):
    inlines = (ComissionNoteItemsInline,)
    exclude = ()


@admin.register(ComissionNoteItems)
class ComissionNoteItemsAdmin(admin.ModelAdmin):
    exclude = ()
