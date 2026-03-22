from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
]
