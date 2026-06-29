from . import views
from django.urls import path

app_name = "posts"


urlpatterns = [
    path("", views.feed, name="feed"),
    path("createpost/", views.create_post, name="createpost"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/", views.like_post, name="like"),
    path("comment/<int:post_id>/", views.comment_post, name="comment"),
    path("search/", views.search_view, name="search"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]
