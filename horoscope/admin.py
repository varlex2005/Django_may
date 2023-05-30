from django.contrib import admin
from .models import Book, Genre, Movie, Category, Tag, Publisher

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'year', 'publisher', 'genre', 'get_tags')

    def get_tags(self, obj):
        tags = obj.tags.all()
        print(tags)
        return '\n'.join([t.title for t in tags])


# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Publisher)


