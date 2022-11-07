from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    s='<h1>my first app</h1>'
    return HttpResponse(s)
