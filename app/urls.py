from django.urls import path
from .views import NewsListView, newslist

urlpatterns = [
    path('news/', NewsListView.as_view(), name='index'),
    path('', newslist, name="newslist")
]
