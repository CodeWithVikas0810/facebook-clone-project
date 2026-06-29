from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import FriendRequest, Friendship, get_friend_ids

User = get_user_model()


@login_required
def friends_view(request):
    """Display friends, friend requests, and friend suggestions."""

    user = request.user

    friend_ids = get_friend_ids(user)
    friends = User.objects.filter(id__in=friend_ids).select_related("profile")

    incoming = FriendRequest.objects.filter(receiver=user).select_related(
        "sender", "sender__profile"
    )

    outgoing = FriendRequest.objects.filter(sender=user).select_related(
        "receiver", "receiver__profile"
    )

    incoming_ids = incoming.values_list("sender_id", flat=True)
    outgoing_ids = outgoing.values_list("receiver_id", flat=True)

    suggestions = User.objects.exclude(
        Q(id=user.id)
        | Q(id__in=friend_ids)
        | Q(id__in=incoming_ids)
        | Q(id__in=outgoing_ids)
    ).select_related("profile")

    context = {
        "friends": friends,
        "incoming": incoming,
        "outgoing": outgoing,
        "suggestions": suggestions,
    }

    return render(request, "friends/friends.html", context)


@login_required
def send_friend_request(request, user_id):
    """Send a friend request."""

    if request.method == "POST":

        receiver = get_object_or_404(User, id=user_id)

        if receiver == request.user:
            return redirect("friends:friends")

        already_friends = Friendship.objects.filter(
            Q(user1=request.user, user2=receiver)
            | Q(user1=receiver, user2=request.user)
        ).exists()

        if already_friends:
            return redirect("friends:friends")

        FriendRequest.objects.get_or_create(
            sender=request.user,
            receiver=receiver,
        )

    return redirect("friends:friends")


@login_required
def accept_friend_request(request, request_id):
    """Accept a friend request."""

    if request.method == "POST":

        friend_request = get_object_or_404(
            FriendRequest,
            id=request_id,
            receiver=request.user,
        )

        user1, user2 = sorted(
            [friend_request.sender, friend_request.receiver],
            key=lambda user: user.id,
        )

        Friendship.objects.get_or_create(
            user1=user1,
            user2=user2,
        )

        friend_request.delete()

    return redirect("friends:friends")


@login_required
def reject_friend_request(request, request_id):
    """Reject a friend request."""

    if request.method == "POST":

        friend_request = get_object_or_404(
            FriendRequest,
            id=request_id,
            receiver=request.user,
        )

        friend_request.delete()

    return redirect("friends:friends")


@login_required
def cancel_friend_request(request, request_id):
    """Cancel the friend request"""
    if request.method == "POST":
        friend_request = get_object_or_404(
            FriendRequest,
            id=request_id,
            sender=request.user,
        )
        friend_request.delete()

    return redirect("friends:friends")


