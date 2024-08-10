from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsModel

class NewsListView(ListView):
    model = NewsModel
    template_name = 'index.html'
