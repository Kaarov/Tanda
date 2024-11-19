from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from users import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('user/update/', views.UpdateUserProfileView.as_view(), name='update-user'),
]
