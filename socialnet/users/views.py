from django.shortcuts import render

from users.forms import LoginForm


# Create your views here.

def user_login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
