from django.db import models

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)


class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self):
        return self.name



class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, verbose_name='Автор')
    summary = models.TextField(max_length=1000, help_text="Краткое описание книги",
                               verbose_name='Аннотация')
    genre = models.ForeignKey(Genre, null=True, help_text="Выберите жанр книги",
                              verbose_name='Жанр', on_delete=models.SET_NULL)
    year_of_writing = models.IntegerField(verbose_name='Год публикациии', null=True)

    # photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.title


