from django.shortcuts import render
from django.http import HttpResponse
from .models import Mkulima


def home(request):
        wakulima = Mkulima.objects.all()
        return render(request, 'home.html', {'wakulima': wakulima})