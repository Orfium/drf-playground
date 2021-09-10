from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.db.models import CASCADE, ForeignKey


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
    owner = ForeignKey(
        User, on_delete=CASCADE, related_name="file_owner", null=True
    )
