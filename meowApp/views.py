from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# creacion de vistas.

# Vista del feed principal
def feed(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'social/feed.html', context)

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'social/login.html', {'form': form})

# Vista de registro de usuario
def register(request):
    if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           raw_password = form.cleaned_data['password1']
           user = authenticate(username=username, password=raw_password)
           if user is not None:
                login(request, user)
           messages.success(request, f'Usuario {username} Creado Correctamente')           
           return redirect('feed')
    else:
         form = UserRegisterForm() 
    context=  { 'form' : form }          
    return render(request, 'social/register.html', context )

# Vista de creacion de post
@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Creado Correctamente')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', { 'form': form }) 

# Vista de perfil de usuario
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        try:
            user = User.objects.get(username=username)
            posts = user.posts.all()
            is_own_profile = False
        except User.DoesNotExist:
            messages.error(request, f'El usuario "{username}" no fue encontrado.')
            return redirect('feed')
    else:
        posts = current_user.posts.all()
        user = current_user
        is_own_profile = True    
    return render(request, 'social/profile.html', {'user':user, 'posts': posts, 'is_own_profile': is_own_profile})

# Vista para seguir a un usuario
def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

# Vista para dejar de seguir a un usuario
def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')