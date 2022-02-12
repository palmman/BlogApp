from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import LoginForm, RegisterForm, AddArticleForm, AddUpdateForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def home(request):
    
    article_list = Article.objects.all().order_by('-published')
    
    context = {
        'article_list':article_list,
    }
    
    return render(request, 'home.html', context)

def article_detail(request, slug):
    
    article = get_object_or_404(Article, slug=slug)
    
    context = {
        'article':article,
    }
    
    return render(request, 'article.html', context)

def user_login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
        else:
            pass
        
        
    return render(request, 'login.html')

def user_register(request):
    
    form = RegisterForm()
    
    if request.method == "POST":
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('user_login')
        else:
            pass
        
    context = {
        'form':form,
    }
    
    return render(request, 'register.html', context)

def user_logout(request):
    
    logout(request)
    
    return redirect('user_login')

def reset_password(request):
    
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            
            user = request.user
            user.set_password(password1)
            user.save()
        
        else:
            return render('reset_password')
        
    return render(request, 'resetpassword.html')

def add_article(request):
    
    user = request.user
    
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = user
            article.save()
            return redirect('home')
        else:
            return message('Please try it again')
    else:
        form = AddArticleForm()
        
    context = {
        'form':form,
    }
        
    return render(request, 'add_article.html', context)

def update_article(request, slug):
    
    article = get_object_or_404(Article, slug=slug)
    form = AddUpdateForm(request.POST or None, instance=article)
    
    
    if form.is_valid():
        form.save()
        return redirect('home')
    
    
    context = {
        'form':form,
    }
    
    return render(request, 'update_article.html', context)

def delete_article(request, slug):
    
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    
    return redirect('home')
    
    
    
        

    
    
    
            
    
    
            
            