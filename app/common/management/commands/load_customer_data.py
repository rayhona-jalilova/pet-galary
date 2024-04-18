from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from accounts.models import Contact
from sales.entity.models import Customer


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "quantity", type=int, help="Add quantity of Customers"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        quantity = options["quantity"]

        for number in range(quantity):
            contact = Contact.objects.create(phone_number="+992004992200")
            Customer.objects.create(
                name=f"Test Testov {number}", contact=contact
            )

        self.stdout.write(
            self.style.SUCCESS(f"Fake Customer data has been loaded.")
        )
