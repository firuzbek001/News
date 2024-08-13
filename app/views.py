from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsModel

class NewsListView(ListView):
    model = NewsModel
    template_name = 'index.html'

def newslist(request):
    news = NewsModel.objects.all()[:5]
    context = {
        'object_list' : news
    }
    return render(request, 'index.html', context)
