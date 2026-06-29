from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from friends.models import get_friend_ids

from .models import Post, Comment
from .forms import PostForm, CommentForm



# Create your views here.


@login_required
def feed(request):
    """Feed showing posts from the logged-in user and their accepted friends."""
    visible_user_ids = get_friend_ids(request.user) + [request.user.id]

    posts = (
        Post.objects.filter(user_id__in=visible_user_ids)
        .select_related("user", "user__profile")
        .prefetch_related(
            "liked_by",
            "comments__user",
            "comments__replies",
            "comments__replies__user",
        )
        .order_by("-created_at")
    )

    form = PostForm()

    return render(request, "posts/feed.html", {"posts": posts, "form": form})


@login_required
def create_post(request):
    """Create a post that will gonna feature in feed"""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    return redirect("posts:feed")


@login_required
def edit_post(request, post_id):
    """If you want to add any improvement in your post"""
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:feed")
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {"form": form})


@login_required
def delete_post(request, post_id):
    """Delete users own post"""
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("posts:feed")
    return render(request, "posts/delete_post.html", {"post": post})


@login_required
def like_post(request, post_id):
    """Action to perform when user likes the post"""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        if post.liked_by.filter(id=request.user.id).exists():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.add(request.user)
    return redirect("posts:feed")


@login_required
def comment_post(request, post_id):
    """Comment on post"""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user

            parent_id = request.POST.get("parent_id")

            if parent_id:
                comment.parent = get_object_or_404(
                    Comment,
                    id=parent_id,
                    post=post,
                )

            comment.save()

    return redirect("posts:feed")

