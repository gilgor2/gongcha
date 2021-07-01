from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from login.models import CustomUser


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    like_posts = models.ManyToManyField('Content', blank=True, related_name='like_users')

    def __str__(self):
        return str(self.user)

class Content(models.Model):
    objects = models.Manager() #에러를 피하기 위해 추가
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField(default='')
    tags = models.ManyToManyField('Tag',blank=True)
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    objects = models.Manager() #에러를 피하기 위해 추가
    post = models.ForeignKey('Content',on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name