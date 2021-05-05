from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
# Create your models here.
class Content(models.Model):
    objects = models.Manager() #에러를 피하기 위해 추가
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default = timezone.now)
    body = models.TextField(default='')

class Comment(models.Model):
    objects = models.Manager() #에러를 피하기 위해 추가
    post = models.ForeignKey('Content',on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)