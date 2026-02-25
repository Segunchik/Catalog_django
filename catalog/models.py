from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=150, verbose_name="Наименование категории", help_text="Введите название категории"
    )
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "category_name",
        ]

    def __str__(self):
        return f"Категория {self.category_name}"


class Product(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    product_image = models.ImageField(
        upload_to="catalog/images", verbose_name="Изображение продукта", blank=True, null=True
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", blank=True, null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "category", "price"]

    def __str__(self):
        return f"Продукт {self.product_name}. Цена: {self.price}"
