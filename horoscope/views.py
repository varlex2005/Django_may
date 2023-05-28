from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h2>Главная</h2>')


def books(request):
    return HttpResponse('Список книг')


def movies(request):
    return HttpResponse('Список фильмов')


