from django.contrib import admin

from ..models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'owner',
    ]

    search_fields = [
        'id',
        'name',
        'owner__username',
    ]

    list_filter = [
        'owner',
    ]

    autocomplete_fields = [
        'owner',
    ]
