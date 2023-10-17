from django.shortcuts import render, redirect
from .models import Post, Profile

from .forms import UserRegisterForm

from django.contrib.auth import logout


def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts

    }
    return render(request, 'twitter/newsfeed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = UserRegisterForm()
    context = { 
        'form' : UserRegisterForm()
    }
    return render(request, 'twitter/register.html', context)


def profile(request):

    return render(request, 'twitter/profile.html')

def editar(request):
    return render(request, 'twitter/editar.html')
