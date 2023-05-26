from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f'Книга: {self.id}  Название:  {self.title} Автор: {self.author}'
#         строковое представление объекта (записи в БД)
oo

# эту таблицу надо теперь записать в БД python3 manage.py makemigrations -
# выполнить в терминале и потом python3 manage.py migrate. Не забыть,
# что в settings.py на 33 строке проверить что само приложение прописано там