from django.urls import reverse_lazy
from django.db import models
from .models import Article
from django.views.generic import ListView,DetailView
from django.views.generic.edit import  UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import (LoginRequiredMixin,UserPassesTestMixin)
# Create your views here.


class ArticleListView(LoginRequiredMixin,ListView):
    model=Article
    template_name='article_list.html'

class ArticleUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Article
    template_name='article_edit.html'
    fields=('title','body')
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model=Article
    template_name='article_detail.html'
    



class ArticleDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user



class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Article
    template_name='article_create.html'
    fields=('title','body')

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

