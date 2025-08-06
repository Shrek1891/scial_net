from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from users.forms import LoginForm


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        print("post")
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user =authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('user logged in')
            else:
                return HttpResponse('user not logged in')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def index(request):
    return render(request, 'users/index.html')


