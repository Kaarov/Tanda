# Generated by Django 4.2 on 2024-11-20 04:33

from django.db import migrations, models
from datetime import time


def seed_time_ranges_and_days(apps, schema_editor):
    # Get the models dynamically to avoid import issues
    TimeRange = apps.get_model('duration', 'TimeRange')
    DayOfWeek = apps.get_model('duration', 'DayOfWeek')

    # Populate time ranges
    for hour in range(24):
        start = time(hour=hour, minute=0)
        end = time(hour=(hour + 1) % 24, minute=0)
        TimeRange.objects.get_or_create(start_time=start, end_time=end)

    # Populate days of the week
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    for day in days:
        DayOfWeek.objects.get_or_create(name=day)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DayOfWeek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                ("name", models.CharField(max_length=10, unique=True)),
            ],
            options={
                "verbose_name": "DayOfWeek",
                "verbose_name_plural": "DayOfWeeks",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="TimeRange",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
            options={
                "verbose_name": "TimeRange",
                "verbose_name_plural": "TimeRanges",
                "ordering": ("-created_at",),
            },
        ),
        migrations.RunPython(
            seed_time_ranges_and_days,
        ),
    ]
