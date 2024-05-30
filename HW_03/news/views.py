from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime

class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    #queryset = Post.title
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class IdPostList(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class AuthorList(ListView):
    model = Author
    ordering = 'ratingAuthor'
    template_name = 'author.html'
    context_object_name = 'author'