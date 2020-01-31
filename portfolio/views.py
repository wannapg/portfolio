from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def main(request):
    return render(request,'main.html')

def courses(request):
    return render(request,'courses.html')

def projects(request):
    return render(request,'projects.html')

def dino(request):
    return render(request,'dino.html')

def resume(request):
    return render(request,'resume.html')