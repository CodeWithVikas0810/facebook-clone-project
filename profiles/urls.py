from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("edit/", views.edit, name="edit"),
    path("", views.profile, name="profile"),
    path("u/<str:username>/", views.user_profile, name="user_profile"),
]
