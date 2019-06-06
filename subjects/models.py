from django.db import models
from django import forms
from django.contrib.auth.models import User


class Subject(models.Model):
    objects = models.Manager()
    
    title = models.CharField(max_length=200)
    content =models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Post(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete = models.CASCADE, related_name='posts')
    wordcount = models.IntegerField(null = True)
    likes_check = models.ManyToManyField(User, related_name = 'likes_check')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

    
class Like(models.Model):
    objects = models.Manager()
    state = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE, related_name='likes')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

class Dislike(models.Model):
    objects = models.Manager()
    state = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE, related_name='dislikes')
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)