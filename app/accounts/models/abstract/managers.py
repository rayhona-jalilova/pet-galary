from typing import Any
from django.contrib.auth.models import BaseUserManager


class UserModelManager(BaseUserManager):
    def create_user(self, email: str, password, **extra_fields):
        if not email:
            raise ValueError("Email is not provided")
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
