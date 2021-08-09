from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('welkam back')


def home(request):
    return HttpResponse('welkam home')