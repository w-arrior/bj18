from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpReponse('index')

def login(request):
    return ('/index')

def print():
    print('python')
