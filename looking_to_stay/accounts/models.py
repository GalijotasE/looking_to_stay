from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=True)
    is_company = models.BooleanField(default=False)
    country = models.CharField(max_length=50, blank=True)