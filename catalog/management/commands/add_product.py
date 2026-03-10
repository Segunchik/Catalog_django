from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add catalog to the database"

    # Удаляем существующие записи
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(
            category_name="Планшеты",
            description="Категория планшетов",
        )

        products = [
            {
                "product_name": "Samsung GALAXY TAB",
                "description": "Классный флагманский планшет",
                "category": category,
                "price": "250",
            },
            {"product_name": "XIAOMI TAB", "description": "Бюджетный планшет", "category": category, "price": "150"},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added catalog: {product.product_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.product_name}"))
