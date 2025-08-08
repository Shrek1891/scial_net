from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PostForm


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
