from django.contrib import admin

from blog.models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "image", "created_at", "is_publishing")
    list_filter = ("is_publishing",)
    search_fields = ("id", "title")
