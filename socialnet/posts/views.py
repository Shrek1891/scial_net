from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from .models import Post
import json


# Create your views here.
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostForm(data=request.GET)
    return render(request, 'post/post_create.html', {'form': form})


def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    posts = Post.objects.all().order_by('-created_at')
    login_user = request.user
    return render(request, 'post/feed.html', {'posts': posts, 'login_user': login_user, "comment_form": comment_form})


def like_post(request):
    print('like_post')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data['post_id']
            post = Post.objects.get(id=post_id)
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            return JsonResponse({'message': 'Like added'}, status=200)
        except:
            return JsonResponse({'message': 'Like not added'}, status=400)
    else:
        return JsonResponse({'message': 'Like not added'}, status=400)
