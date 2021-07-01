from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from .models import BlogModel
from django.urls import reverse_lazy
# Create your views here.

class BlogPageView(ListView):
    model=BlogModel
    template_name='index.html'
    context_object_name='posts'


class BlogDetailView(DetailView):
    model=BlogModel
    template_name='post_detail.html'

class BlogUpdateView(UpdateView):
    model=BlogModel
    template_name='post_update.html'
    fields=['title','content','image']


class BlogDeleteView(DeleteView):
    model=BlogModel
    template_name='delete_post.html'
    success_url =reverse_lazy('home')


class BlogCreateView(CreateView):
    model=BlogModel
    template_name='blog_add.html'
    fields=['title','content','user','image']

    

   
    