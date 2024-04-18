from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from inventory.entity.models import Product, ProductDetail, Category


class Command(BaseCommand):
    help = "Load fake Product data to database."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("quantity", type=int, help="Quantity of products")

    def handle(self, *args: Any, **options: Any) -> str | None:
        quantity = options["quantity"]
        # Assuming category_initial_code and category_last_code are unique for each Category instance
        category = Category.objects.create(
            name="Test category",
            category_initial_code=1000 + quantity,
            category_last_code=2000 + quantity,
        )

        for i in range(quantity):
            product = Product.objects.create(
                name=f"Fake Product {i}", category=category
            )

            product_detail = ProductDetail.objects.create(
                product=product,
                price=i * 10,
                selling_price=i * 11,
                quantity=i * 5,
                measurement="piece",
            )

            self.stdout.write(
                self.style.SUCCESS(f"Fake product data created successfully.")
            )
