from django.shortcuts import render,redirect,get_object_or_404
from .models import Subject, Post, Like
from .forms import SubjectForm, PostForm, LikeForm, DislikeForm



def new_subeject(request):
    return render(request,'subjects/new_subject.html')
    

def create_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('home')
    return render(request,'subjects/create_subject.html',{'form':form})
    

def show_subject(request, id):
    subject = get_object_or_404(Subject,pk=id)
    return render(request,'subjects/show_subject.html',{'subject':subject})
    

def update_subject(request, id):
    subject = get_object_or_404(Subject,pk=id)
    if request.method == "POST":
        content = request.POST.get('content')
        subject.content = content
        subject.save()
        return redirect('show_subject',subject.id)
    return render(request,'subjects/update_subject.html',{'subject':subject})
        
    
def delete_subject(request, id):
    subject = get_object_or_404(Subject,pk=id)
    subject.delete()
    return redirect('home')
    
    
def new_post(request,id):
    subject = get_object_or_404(Subject,pk=id)
    return render(request,'subjects/new_post.html',{'subject':subject})
    

def create_post(request, id):
    subject = get_object_or_404(Subject,pk=id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.subject = subject
            form.user = request.user
            form.wordcount=len(form.content.split())
            form.save()
            return redirect('show_subject',subject.id)
    return render(request, 'subjects/new_post.html',{'form' : form})
    

def update_post(request, id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        content = request.POST.get('content')
        post.content = content
        post.wordcount=len(post.content.split())
        post.save()
        return redirect('show_subject',post.subject.id)
    return render(request,'subjects/update_post.html',{'post':post})
    
    
def delete_post(request, id):
    post = get_object_or_404(Post,pk=id)
    subject = post.subject
    post.delete()
    return render(request,'subjects/show_subject.html',{'subject':subject})
 

def create_like(request, id):
    post = get_object_or_404(Post,pk=id)
    subject = post.subject
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.post = post
            form.user = request.user
            form.save()
            return redirect('show_subject',subject.id)
    return render(request, 'subjects/new_like.html',{'form' : form})
    
 
def create_dislike(request, id):
    post = get_object_or_404(Post,pk=id)
    subject = post.subject
    if request.method == "POST":
        form = DislikeForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.post = post
            form.user = request.user
            form.save()
            return redirect('show_subject',subject.id)
    return render(request, 'subjects/new_like.html',{'form' : form})
    
def likes_check(request, id):
    user = request.user
    post = get_object_or_404(Post,pk=id)
    subject = post.subject
    if request.method == 'POST':
        if post.likes_check.filter(id = user.id).exists():
            post.likes_check.remove(user)
        else :
            post.likes_check.add(user)
    return redirect('show_subject',subject.id)
    
def like_list(request):
    return render(request,'subjects/like_list.html')
    
    