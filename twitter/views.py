from django.shortcuts import render, redirect
from .models import Post, Profile

from .forms import UserRegisterForm, PostForm

from django.contrib.auth import logout


def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'form': PostForm

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

def eliminar(request, post_id):
    post = Post.objects.filter(id=post_id)
    post.delete()
    return redirect('home')
