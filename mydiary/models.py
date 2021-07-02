from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from login.models import CustomUser


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    bio = models.TextField(default='', blank=True)
    birthday = models.DateField(default = timezone.now ,null=True)
    like_posts = models.ManyToManyField('Content', blank=True, related_name='like_posts_profile')

    def __str__(self):
        return str(self.user)

class Content(models.Model):
    objects = models.Manager() #에러를 피하기 위해 추가
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name = 'author_content')
    pub_date = models.DateTimeField(default = timezone.now)
    limit = models.IntegerField(default=0)
    body = models.TextField(default='', max_length="100")
    tags = models.ManyToManyField('Tag',blank=True)
    
    like_users = models.ManyToManyField(Profile, blank=True, related_name = 'like_users_content')
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