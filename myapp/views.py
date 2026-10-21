from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("<h1>Hello, World! This is the home page of my Django app.</h1>")


def about(request):
    return HttpResponse("<h1>This is the about page of my Django app.</h1>")
