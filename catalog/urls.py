
from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ProductListView, ProductDetailView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
#    path("", RedirectView.as_view(url="/product_list/", permanent=False), name="root"),
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
