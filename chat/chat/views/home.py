from django.shortcuts import render


def home_handler(request, asdf):
    return render(request, 'home.html', {'asdf':'asdf'})
