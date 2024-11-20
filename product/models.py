from django.db import models
from django.utils.text import slugify
from config.models import TimestampedModel


class Category(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField("Slug", unique=True, blank=True)
    photo = models.ImageField("Image", upload_to="category/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(TimestampedModel):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField("Slug", unique=True, blank=True)
    photo = models.ImageField("Image", upload_to="subcategory/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
