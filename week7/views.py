from django.shortcuts import render
from subjects.models import Subject

def home(request):
    subjects = Subject.objects.all()
    return render(request,'home.html',{'subjects':subjects})
    
    