from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator

from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'phone_number', 'email']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise AuthenticationFailed("Invalid phone number or password.")

        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class RegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^\+996\d{9}$",
                message="Phone number must be in the format '+996XXXXXXXXX'."
            )
        ]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"}
    )
    business = serializers.BooleanField(required=False, default=False)

    class Meta:
        model = User
        fields = ["phone_number", "password", "confirm_password", "business"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        business = validated_data.pop('business', False)
        try:
            user = User.objects.create_user(
                phone_number=validated_data["phone_number"],
                password=validated_data["password"],
                business=business,
            )
            self.instance = user
            return user
        except IntegrityError as e:
            raise AuthenticationFailed(e)


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\+996\d{9}$',
                message="Phone number must be in the format '+996XXXXXXXXX'."
            )
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'avatar', 'phone_number', 'email']

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return value
