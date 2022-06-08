from django.contrib import admin

from .models import ComissionNote, ComissionNoteItems


class ComissionNoteItemsInline(admin.TabularInline):
    model = ComissionNoteItems
    extra = 0


@admin.register(ComissionNote)
class ComissionNoteAdmin(admin.ModelAdmin):
    inlines = (ComissionNoteItemsInline,)
    list_display = (
        '__str__',
        'created_by',
        'employee',
        'payment_date',
        'paid',
        'active'
    )
    readonly_fields = ('created_by',)
    search_fields = ('created_by__first_name', 'employee__first_name')
    list_filter = ('paid', 'active')
    date_hierarchy = 'created'
    ordering = ('-created',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.save()
        super(ComissionNoteAdmin, self).save_model(request, obj, form, change)


@admin.register(ComissionNoteItems)
class ComissionNoteItemsAdmin(admin.ModelAdmin):
    exclude = ()
