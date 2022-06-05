from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .models import Post
from .models import Profile



# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def postedit(request):
    if request.method == 'POST':
        
        title = request.POST['title']
        body = request.POST['body']
        #test=request.POST['test']
        post1 = Post.objects.create(title = title, body = body, author=request.user)
        post1.save()
        return redirect('index')
    else:
        return render(request, 'postedit.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

