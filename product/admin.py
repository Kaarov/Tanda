from django.contrib import admin

from .models import Category, SubCategory


@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by name"


@admin.register(SubCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by name"
