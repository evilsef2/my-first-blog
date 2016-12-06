# coding: utf-8
from blog.models import Post 
from django.shortcuts import render
from django.utils import timezone


#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {})



from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

#from django.shortcuts import render

#def post_list(request):
#	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

from blog.forms import PostForm

def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})