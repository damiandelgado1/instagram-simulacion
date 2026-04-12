from django.contrib import admin
from post.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "text", "created_at"]