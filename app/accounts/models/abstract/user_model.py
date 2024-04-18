from django.db import models
from .managers import UserModelManager
from accounts.models.abstract import AbstractUserModel


class User(AbstractUserModel):
    is_user = models.BooleanField(default=True, null=True, blank=True)

    objects = UserModelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
