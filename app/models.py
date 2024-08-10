from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()