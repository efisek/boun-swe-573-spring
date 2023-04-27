from django.contrib.auth.models import UserManager
from django.db import models


class User(models.Model):
    username = models.CharField(("Username"),max_length=25, unique=True, blank=False)
    email = models.EmailField(("Email"),max_length=25, unique=True, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)