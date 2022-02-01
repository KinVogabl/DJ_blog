from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    tags = TaggableManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    text = models.TextField(max_length=250)
    active = models.BooleanField(default=True)



    def __str__(self):
        return self.username

