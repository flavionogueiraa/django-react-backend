from django.contrib import admin

from ..models import ListItem


@admin.register(ListItem)
class ListItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'list',
        'done',
    ]

    search_fields = [
        'id',
        'name',
        'list__name',
    ]

    list_filter = [
        'list',
        'done',
    ]

    autocomplete_fields = [
        'list',
    ]
