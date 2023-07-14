from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))

with open('data-398-2018-08-30.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    station = [row for row in reader]


def bus_stations(request):
    try:
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(station, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page
        }
        return render(request, 'stations/index.html', context)
    except Exception:
        print("BAD REQUEST!!!")

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    # context = {
    #     'bus_stations': ...,
    #     'page': ...,
    # }