from django.shortcuts import get_object_or_404, render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Like


@login_required
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


@login_required
def create_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('all_posts')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'single_post.html', {'post': post})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('single_post', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')

    return render(request, 'delete_post.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has already liked the post
    existing_like = Like.objects.filter(user=user, post=post).first()

    if existing_like:
        # If the user has already liked the post, remove the like
        existing_like.delete()
    else:
        # If the user hasn't liked the post yet, create a new like
        Like.objects.create(user=user, post=post)

    return redirect('single_post', post_id=post.id)
