from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    body=models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
