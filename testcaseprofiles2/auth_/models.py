import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eye = models.CharField(max_length=20, blank=True, default='', null=True)
    country = models.CharField(max_length=20, blank=True, default='', null=True)
