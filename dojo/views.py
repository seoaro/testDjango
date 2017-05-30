# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

#def mysum(request, x, y=0, z=0):
    # request: HttpRequest
    #return HttpResponse(int(x) + int(y) + int(z))

def mysum(request, numbers):
    # numbers = "1/23/3143/32131251/123"
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('Hi, {}. {} years old.'.format(name, age))
