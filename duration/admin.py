from django.contrib import admin
from duration import models


@admin.register(models.TimeRange)
class UserAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('start_time',)
    list_filter = ('is_active',)
    list_display_links = ("start_time",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by start time"


@admin.register(models.DayOfWeek)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_display_links = ("name",)
    list_per_page = 10
    ordering = ("-id",)
    search_help_text = "Search by name"
