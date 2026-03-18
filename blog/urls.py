
from django.urls import path
from django.views.generic import RedirectView

from blog.apps import BlogConfig
from blog.views import PostsListView, PostCreateView, PostUpdateView, PostDetailView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
#    path("", RedirectView.as_view(url="/product_list/", permanent=False), name="root"),
    path("", PostsListView.as_view(), name="posts_list"),
    path("posts/create", PostCreateView.as_view(), name="posts_create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/detail/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_confirm_delete"),
    # path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
