from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)
    is_active = models.BooleanField("Active", default=True)

    class Meta:
        abstract = True
        get_latest_by = "updated_at"
