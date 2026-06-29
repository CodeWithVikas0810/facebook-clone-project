from django.db import models
from django.conf import settings



# Create your models here.
class Profile(models.Model):
    """This is user model for profile picture"""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=300, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    cover_picture = models.ImageField(upload_to="cover_photos/", blank=True, null=True)

    def __str__(self):
        return self.user.username
