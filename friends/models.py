from django.db import models
from django.db.models import Q
from django.conf import settings


def get_friend_ids(user):
    """Return a list of user IDs that are accepted friends of the given user."""
    friendships = Friendship.objects.filter(Q(user1=user) | Q(user2=user))

    friend_ids = []
    for friendship in friendships:
        if friendship.user1_id == user.id:
            friend_ids.append(friendship.user2_id)
        else:
            friend_ids.append(friendship.user1_id)

    return friend_ids


# Create your models here.
class FriendRequest(models.Model):
    """Friend request send from one user to another"""

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sent_request", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="received_request",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        """Only one pending or accepted request per sender-receiver pair"""

        constraints = [
            models.UniqueConstraint(
                fields=["sender", "receiver"], name="unique_friend_request"
            )
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"


class Friendship(models.Model):
    """Represents an accepted friendship."""

    user1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="friendships_as_user1",
        on_delete=models.CASCADE,
    )

    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="friendships_as_user2",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user1", "user2"],
                name="unique_friendship",
            )
        ]

    def __str__(self):
        return f"{self.user1} ↔ {self.user2}"
