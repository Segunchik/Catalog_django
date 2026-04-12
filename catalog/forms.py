from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["is_publish", "owner"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["product_name"].help_text = None
        self.fields["category"].label = "Категория"
        self.fields["price"].label = "Цена"

        self.fields["product_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название товара"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "rows": 5, "placeholder": "Введите описание товара"}
        )
        self.fields["product_image"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Введите цену"})

    def clean(self):
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        cleaned_data = super().clean()
        product_name = cleaned_data.get("product_name")
        description = cleaned_data.get("description")

        for word in forbidden_words:
            if word in product_name.lower():
                self.add_error("product_name", f"Недопустимое слово: {word}")
            if word in description.lower():
                self.add_error("description", f"Недопустимое слово: {word}")
        return cleaned_data

    def clean_price(self):
        """Валидация поля price"""
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("is_publish",)
        # fields = "__all__"
        # exclude = ["owner"]


class ProductModeratorOwnerForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["owner"]


class ProductSuperuserForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


