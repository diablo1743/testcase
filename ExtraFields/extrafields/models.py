import uuid
from django.db import models


class ExtraFieldAbstract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(unique=True, max_length=100, blank=False, default='Russia', db_index=True)
    description = models.TextField(max_length=100, null=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class EyeColor(ExtraFieldAbstract):
    pass
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Country(ExtraFieldAbstract):
    pass
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
