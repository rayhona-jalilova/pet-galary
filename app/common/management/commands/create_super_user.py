from typing import Any
from django.core.management.base import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    help = "Create super user."

    def handle(self, *args: Any, **options: Any) -> str | None:
        User.objects.create_superuser(email="test@test.com", password="2023")

        self.stdout.write(
            self.style.SUCCESS(
                "Superuser with email test@test.com and password 2023 has been created"
            )
        )
