from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
def cart(request):
    return HttpResponse('This is Cart page')

def profile(request):
    return HttpResponse('This is Profile page')

def payment(request):
    return HttpResponse('This is Payments page')