from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'name': 'Kjell'}
    return render(request, 'pygrounds/index.html', context)
