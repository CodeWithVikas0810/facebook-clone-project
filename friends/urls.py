from django.urls import path
from . import views

app_name = "friends"


urlpatterns = [
    path("", views.friends_view, name="friends"),
    path("send/<int:user_id>/", views.send_friend_request, name="send_request"),
    path(
        "accept/<int:request_id>/",
        views.accept_friend_request,
        name="accept_request",
    ),
    path(
        "reject/<int:request_id>/",
        views.reject_friend_request,
        name="reject_request",
    ),
    path("cancel/<int:request_id>",views.cancel_friend_request,name="cancel_request")    
]
