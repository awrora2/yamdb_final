from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Category_name'
    )
    slug = models.SlugField(
        max_length=50,
        primary_key=True,
        verbose_name='slug_name'
    )

    class Meta:
        ordering = ['slug', ]
        verbose_name = 'Category'

    def __str__(self):
        return f'{self.name}: {self.slug}'


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Genre_name'
    )
    slug = models.SlugField(
        max_length=50,
        primary_key=True,
        verbose_name='Genre_slug_name',
    )

    class Meta:
        verbose_name = 'Genre'

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Title_name'
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(datetime.now().year)],
        verbose_name='Year_of_production'
    )
    description = models.CharField(
        blank=True,
        max_length=256,
        verbose_name='Title_description',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        verbose_name='Title_category',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
    )

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Title'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)])

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.author.username


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
