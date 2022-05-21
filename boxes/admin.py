from django.contrib import admin
from .models import Box, Category


class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Box, BoxAdmin)
admin.site.register(Category, CategoryAdmin)
