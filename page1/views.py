from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)


def team(request):
    context = {}
    return render(request, 'team.html', context)
