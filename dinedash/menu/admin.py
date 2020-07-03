"""
This module connects the app's models to the Django admin interface
"""
from django.contrib import admin

from .models import Addon, AddonSection, Menu, MenuCategory, MenuItem

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(AddonSection)
admin.site.register(Addon)


class CategoryInline(admin.TabularInline):
    """Shows categories inline for easier adding"""

    model = MenuCategory
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Defines the admin section for Menus"""

    inlines = [
        CategoryInline,
    ]
