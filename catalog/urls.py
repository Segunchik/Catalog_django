from django.urls import path
from django.views.generic import RedirectView

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False), name='root'),
    path("home/",views.home, name="home"),
    path("contacts/",contacts, name="contacts"),

]