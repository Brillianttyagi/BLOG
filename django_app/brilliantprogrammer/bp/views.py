from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contactus.html')


def about(request):
    return render(request,'aboutus.html')

def post(request):
    return render(request,'post.html')