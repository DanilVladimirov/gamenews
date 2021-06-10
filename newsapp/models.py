from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    img = models.ImageField()
    title = models.CharField(default='Новина', max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='news')
    date = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField('Comment', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comment')
    text = models.TextField()

    def __str__(self):
        return f'{self.text[:10]}...'


class Contact(models.Model):
    title = models.CharField(default='', max_length=100)
    text = models.TextField(default='')


class Videos(models.Model):
    title_img = models.ImageField()
    video = models.FileField()
    title = models.CharField(default='', max_length=255)
    comments = models.ManyToManyField(Comment, blank=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='videos')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    theme = models.CharField(default='', max_length=250)
    text = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='feedback')

    def __str__(self):
        return self.theme
