from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(models.Model):
    user = models.OneToOneField(
        DjangoUser,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )


class Details(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)
    permissions = models.CharField(max_length=3, default="644", null=True)
    owner = models.ForeignKey(
        "auth.User", related_name="files", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
