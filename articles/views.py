from django.shortcuts import render

from . models import Article

from django.views.generic import ListView,CreateView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"
    login_url='login'


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    login_url='login'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = "article_edit.html"
    login_url='login'

    def test_func(self):
        obj=self.get_object()
        return self.request.user==obj.author

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url=reverse_lazy('article_list')
    login_url='login'

    def test_func(self):
        obj=self.get_object()
        return self.request.user==obj.author

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article_new.html"
    fields=('title','body')
    login_url='login'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)