from rest_framework import serializers

from duration import models


class TimeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeRange
        fields = "__all__"


class DayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DayOfWeek
        fields = "__all__"
