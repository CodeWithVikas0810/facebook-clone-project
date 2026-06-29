from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import EditProfileForm
from .models import Profile

User = get_user_model()


@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(
        request, "profiles/profile.html", {"profile": profile, "is_owner": True}
    )


@login_required
def user_profile(request, username):
    """Public profile page for any user, reached by clicking their name/avatar."""
    if username == request.user.username:
        return redirect("profiles:profile")

    profile = get_object_or_404(
        Profile.objects.select_related("user"), user__username=username
    )
    return render(
        request, "profiles/profile.html", {"profile": profile, "is_owner": False}
    )


@login_required
def edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profiles:profile")
        else:
            messages.error(request, "Please fix the errors below.")

    else:
        form = EditProfileForm(instance=profile)

    return render(request, "profiles/edit.html", {"form": form})