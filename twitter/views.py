from django.shortcuts import render, redirect
from .models import Post, Relationships

from django.contrib.auth.models import User

from .forms import UserRegisterForm, PostForm , ProfileUpdateForm, UserUpdateForm



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

def eliminar(request, post_id):
    post = Post.objects.filter(id=post_id)
    post.delete()
    return redirect('home')

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

def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'twitter/editar.html', context)

def follow(request, username):

    current_user = request.user
    to_user= User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationships(from_user=current_user, to_user=to_user)
    rel.save()
    return redirect('home')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username) 
    to_user_id = to_user.id
    rel = Relationships.objects.filter(from_user=current_user, to_user=to_user_id)  
    rel.delete()
    return redirect('home')



