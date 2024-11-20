from rest_framework.generics import ListAPIView
from .models import TimeRange, DayOfWeek
from duration import serializers


class TimeRangeDetailListAPIView(ListAPIView):
    queryset = TimeRange.objects.all()
    serializer_class = serializers.TimeRangeSerializer


class DayOfWeekDetailListAPIView(ListAPIView):
    queryset = DayOfWeek.objects.all()
    serializer_class = serializers.DayOfWeekSerializer
