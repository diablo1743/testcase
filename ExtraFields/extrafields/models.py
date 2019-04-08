import uuid
from django.db import models


class ExtraFieldAbstract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=100, blank=False, db_index=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class EyeColor(ExtraFieldAbstract):
    pass


class Country(ExtraFieldAbstract):
    pass
