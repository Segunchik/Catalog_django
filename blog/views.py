from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import Posts


class PostsListView(ListView):
    model = Posts
    template_name = "blog/posts_list.html"

    def get_queryset(self):
        """Сортировка и фильтрация"""
        queryset = super().get_queryset()
        queryset = queryset.filter(is_publishing=True)
        return queryset.order_by("-created_at")


class PostDetailView(DetailView):
    model = Posts
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:posts_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Posts
    fields = ("title", "content", "image")
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:posts_list")


class PostUpdateView(UpdateView):
    model = Posts
    fields = ("title", "content", "image")
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:posts_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Posts
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:posts_list")
