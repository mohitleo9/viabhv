from django.shortcuts import render, redirect
from chitchat.models import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def home_handler(request):
    """
    Basic home page
    """
    username = request.user.username
    return render(request, 'home.html', {'username': username})


def login_handler(request):
    """
    Handles the login page and submission both
    and the asdf is just a side effect of the regex used for
    url and can be ignored
    """

    if request.method == 'POST':
        # login page was used and it is trying to submit
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # take to home page
                    return redirect('home')

    else:
        # create new form for user
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_handler(request):
    """
    Logout user
    """
    logout(request)
    return redirect('home')
