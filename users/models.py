from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

from config.models import TimestampedModel

phone_regex = RegexValidator(
    regex=r"^\+996\d{9}$",
    message="Phone number must be entered in the format: '+996XXXXXXXXX'."
)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number is required.")
        extra_fields.setdefault('is_active', True)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('business', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number=phone_number, password=password, **extra_fields)


class User(AbstractUser, TimestampedModel):
    """User model"""

    phone_number = models.CharField(
        "Phone Number",
        max_length=16,
        unique=True,
        validators=[phone_regex],
    )  # To store numbers like +996 XXX XXX XXX
    email = models.EmailField(
        "Email Address",
        unique=True,
        blank=True,
        null=True
    )
    username = models.CharField(
        "Username",
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )
    company = models.CharField(
        "Company",
        max_length=100,
        blank=True,
        null=True,
    )
    business = models.BooleanField(
        "Business",
        max_length=100,
        default=False,
    )
    avatar = models.ImageField(
        "Avatar",
        upload_to='users-avatar/',
        blank=True,
        null=True,
    )

    # username = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        business = "BusinessUser" if self.business else "Customer"
        return f"{self.phone_number} - {business}"
