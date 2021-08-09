from django.shortcuts import render
from .models import Roads
# Create your views here.


def index(request):
    roads = Roads.objects.all()
    return render(request, 'index.html', {'roads': roads})
