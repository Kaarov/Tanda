from django.contrib import admin

from product import models


@admin.register(models.Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by name"


@admin.register(models.SubCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by name"


@admin.register(models.Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'subcategory', 'address', 'price', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('user',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by user"
