from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    info = Blog.objects.all()
    return render(request,'index.html',{'info':info})

def contact(request):
    return render(request,'contactus.html')


def about(request):
    return render(request,'aboutus.html')

def post(request):
    return render(request,'post.html')