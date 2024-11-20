from django.db import models
from config.models import TimestampedModel


class TimeRange(TimestampedModel):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

    class Meta:
        verbose_name = "TimeRange"
        verbose_name_plural = "TimeRanges"
        ordering = ("-created_at",)


class DayOfWeek(TimestampedModel):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "DayOfWeek"
        verbose_name_plural = "DayOfWeeks"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
