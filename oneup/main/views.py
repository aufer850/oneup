from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request,'main/about.html')

def review(request):
    return render(request,'main/review.html')

def selection(request):
    return render(request,'main/selection.html')

def article(request):
    return render(request,'main/article.html')