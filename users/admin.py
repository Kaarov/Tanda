from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "phone_number",
        "username",
        "business",
    ]
    list_display_links = [
        "phone_number",
    ]
    list_per_page = 10
    search_fields = [
        "phone_number",
        "business",
    ]
    ordering = [
        "-id",
    ]
    search_help_text = "Поиск по номеру телефона"
