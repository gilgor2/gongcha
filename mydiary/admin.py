# mydiary/admin.py
from django.contrib import admin
from .models import Profile, Content, Comment, Tag

admin.site.register(Profile)
admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Tag)