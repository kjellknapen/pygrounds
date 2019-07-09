from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to my pygrounds. This is the start of my website")