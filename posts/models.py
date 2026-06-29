from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your models here.
class Post(models.Model):
    """Creating Post"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    post_picture = models.ImageField(upload_to="posts_pictures/", blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_posts", blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"


class Comment(models.Model):
    """Having comment model for comment and threaded comment functionality"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )

    content = models.TextField(max_length=500)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_comments", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Configuration and indexing for faster data access"""

        ordering = ["created_at"]
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["parent"]),
            models.Index(fields=["created_at"]),
        ]

    def like_count(self):
        """Return the number of likes for this comment"""
        return self.likes.count()

    def __str__(self):
        """Return the username with comment and its comment"""
        return f"{self.user.username}: {self.content[:20]}"
