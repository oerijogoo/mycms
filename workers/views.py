from django.shortcuts import render
from .models import Worker
# Create your views here.


def index(request):
    workers = Worker.objects.all()
    return render(request, 'workers/index.html', {'workers': workers})
