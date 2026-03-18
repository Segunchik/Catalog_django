from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import Posts

class PostsListView(ListView):
    model = Posts
    template_name = "blog/posts_list.html"

class PostDetailView(DetailView):
    model = Posts
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:post_list")


class PostCreateView(CreateView):
    model = Posts
    fields = ("title", "content", "image")
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:posts_list")


class PostUpdateView(UpdateView):
    model = Posts
    fields = ("title", "content", "image")
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:posts_list")


class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy("blog:posts_list")
