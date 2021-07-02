# mydiary/forms.py
from django import forms
from .models import Content, Comment, Tag, Profile

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'limit', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'bio','birthday', ]