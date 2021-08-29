from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'message':'Hello'
    }
    return render(request,'app/index.html',context)

def login(request):
    return render(request,'app/login.html')