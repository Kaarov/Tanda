from django.db import models
from config.models import TimestampedModel
from users.models import User
from duration.models import TimeRange, DayOfWeek


class Category(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    photo = models.ImageField("Image", upload_to="category/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class SubCategory(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    photo = models.ImageField("Image", upload_to="subcategory/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class Product(TimestampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Owner'
    )
    description = models.TextField("Description", null=True, blank=True)
    name = models.CharField("name", max_length=255)
    photo = models.ImageField("Image", upload_to="product/")
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Subcategory',
    )
    address = models.TextField("Address")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.ForeignKey(
        TimeRange,
        on_delete=models.CASCADE,
        related_name='start_time_products',
        verbose_name='Start time',
    )
    end_time = models.ForeignKey(
        TimeRange,
        on_delete=models.CASCADE,
        related_name='end_time_products',
        verbose_name='End time',
    )
    start_day = models.ForeignKey(
        DayOfWeek,
        on_delete=models.CASCADE,
        related_name='start_day_products',
        verbose_name='Start day',
    )
    end_day = models.ForeignKey(
        DayOfWeek,
        on_delete=models.CASCADE,
        related_name='end_day_products',
        verbose_name='End day',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
