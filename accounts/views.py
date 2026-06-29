from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from .forms import SignupForm, LoginForm
from .services import UserService

# Create your views here.


def signup_view(request):
    """Creating a signup page"""

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            UserService.create_user(form)

            messages.success(request, "Account Created Successfully")

            return redirect("accounts:login")
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    """Creating login page"""

    if request.user.is_authenticated:
        return redirect("profiles:profile")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            user = UserService.authenticate_user(
                form.cleaned_data["username"], form.cleaned_data["password"]
            )

            if user:
                login(request, user)
                messages.success(request, "Welcome back!")
                return redirect("profiles:profile")

            messages.error(request, "Invalid username or password")

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


@login_required
def logout_view(request):
    """Creating the logout page"""
    logout(request)
    return redirect("accounts:login")
