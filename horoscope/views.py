from django.shortcuts import render
from django.http import HttpResponse
from horoscope.models import Book, Genre, Publisher

# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)


def books(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()

    return render(request, 'books.html', context={
        'books': books,
        'genres': genres,
        'publishers': publishers,
    })


def movies(request):
    return render(request, 'movies.html', context=None)


