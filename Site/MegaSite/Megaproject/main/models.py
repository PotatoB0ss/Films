from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from embed_video.fields import EmbedVideoField

class Films(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Фильм')
    content = models.TextField(verbose_name='Описание фильма')
    img = models.ImageField(upload_to='uploads',
                            null=True,
                            verbose_name='Картинка')
    genre = models.ManyToManyField('Genres',
                                   verbose_name='Жанры')
    year = models.PositiveIntegerField(verbose_name='Год выхода')
    slug = models.SlugField(max_length=255,
                            unique=True,
                            verbose_name='URL')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Добавлен')

    video = EmbedVideoField(null=True, verbose_name='URL Фильма')


    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['-published']

    def __str__(self):
        return self.title

class Genres(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Жанр')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Films', on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)


    def __str__(self):
        return self.user.username