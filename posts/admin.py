from django.contrib import admin
from .models import Post,Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
    )
    search_fields = (
        "user__username",
        "content",
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "post",
        "created_at",
        "content"
    )
    search_fields = (
        "user__username",
        "content",
        "post_content"
    )