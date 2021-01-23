from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Multiline string with quotes
    return HttpResponse("Rango says hey there partner!"
     "<a href='/rango/about/'>Learn more<a/>")

def about(request):
    # Multiline string with backslash (less common?)
    return HttpResponse("What is my purpose in life?\
     <a href='/rango/'>Go back</a>")
