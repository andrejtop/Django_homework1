from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request) -> str:
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = None
    msg = f"Текущее время: {datetime.datetime.now().time()} <a{reverse('home')}</a>"
    return HttpResponse(msg)


def workdir_view(request) -> str:
    # Получаем список содержимого директории
    contents = os.listdir(path='.')
    all_dir_files = "\n///".join(contents)

    return HttpResponse(all_dir_files)

