from django.urls import path
from duration import views

urlpatterns = [
    path('time-ranges/', views.TimeRangeDetailListAPIView.as_view(), name='time-range-list'),
    path('days/', views.DayOfWeekDetailListAPIView.as_view(), name='day-list'),
]
