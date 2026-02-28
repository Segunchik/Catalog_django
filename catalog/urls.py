
from django.urls import path
from django.views.generic import RedirectView

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
#    path("", RedirectView.as_view(url="/product_list/", permanent=False), name="root"),
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path("product_detail/<int:pk>/", product_detail, name="product_detail"),
]
