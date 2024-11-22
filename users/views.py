from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status

from .serializers import (
    CustomTokenObtainPairSerializer,
    RegistrationSerializer,
    UserProfileSerializer,
    UserProfileUpdateSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class UpdateUserProfileView(APIView):
    serializer_class = UserProfileUpdateSerializer

    def put(self, request):
        user = request.user
        serializer = UserProfileUpdateSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully", "user": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
