from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/workdir_view.html'
    path = '.'
    pages = workdir_files(path)
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def workdir_files(path):
    pages = []
    for enter in os.listdir(path):
        pages.append(enter)
    return pages
