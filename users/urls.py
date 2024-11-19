from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
