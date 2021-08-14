from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm
from .models import Post

def home(request):
    template = 'blog/home.html'
    posts = Post.objects.all().order_by('-updated')
    context = {
                'posts': posts,
            }
    return render(request,template,context)

@login_required(login_url='/accounts/login/') 
def create(request):
    template = 'blog/create.html'
    form = PostCreateForm()
    

    if request.method == 'POST':
        post_create = PostCreateForm(request.POST)
        if post_create.is_valid():
            
            post_create.save()
            messages.success(request, f'Your Post is created successfully !')
            return redirect('User:home')   
    context = {
        'form':form,
    }
    return render(request,template,context)