from django import forms
from .models import Subject, Post, Like, Dislike 

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'title',
            'content'
        ]
        labels = {
            'title': "제목",
            'content': "내용"
        }
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content',
        ]
        labels = {
            'content': "내용",
        }

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = [
            'state',
        ]
        labels = {
            'state': "상태",
        }

class DislikeForm(forms.ModelForm):
    class Meta:
        model = Dislike
        fields = [
            'state',
        ]
        labels = {
            'state': "상태",
        }