from django.shortcuts import render, redirect
from .models import Post, Profile

from django.contrib.auth.models import User

from .forms import UserRegisterForm, PostForm 



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


def profile(request, username):

    user = User.objects.get(username=username)
    post = user.posts.all()

    context = {
        'user' : user,
        'posts': post
    }
    
    print(context)
    return render(request, 'twitter/profile.html', context)

def editar(request):
    return render(request, 'twitter/editar.html')

def eliminar(request, post_id):
    post = Post.objects.filter(id=post_id)
    post.delete()
    return redirect('home')
