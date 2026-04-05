from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


# from users.views import


from users.apps import UsersConfig
from users.views import UserCreateView

app_name = UsersConfig.name


# class UserRegisterView:
#     pass


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html", next_page="/"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    # path("catalog/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    # path("catalog/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    # path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
]
