from django.shortcuts import render

from django.http import HttpResponse

def index_view(request) :
    return HttpResponse('<h1>home page</h1>')

def about_view(request) :
    return HttpResponse('<h1>about page</h1>')

def contact_view(request) :
    return HttpResponse('<h1>contact page</h1>')

# Create your views here.
