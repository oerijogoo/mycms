from django.shortcuts import render
from .models import City


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'city/pie_chart.html', {
        'labels': labels,
        'data': data,
    })
