from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Post

@login_required
def create_post(request):
    if not request.user.has_perm("posts.add_post"):
        return HttpResponseForbidden("You don't have permission to add posts.")

    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            body=request.POST["body"],
            author=request.user,
        )
        return redirect("home")

    return render(request, "posts/create_post.html")

def post_list(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, "posts/post_list.html", {"posts": posts})