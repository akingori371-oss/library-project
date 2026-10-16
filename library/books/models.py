from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Nonfiction'),
        ('scifi', 'Sci-Fi'),
        ('mystery', 'Mystery'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name='books')
    genre = models.CharField(max_length=20 , choices=GENRE_CHOICES,default='fiction')
    published_year = models.IntegerField()
    rating = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    summary = models.TextField(blank=True)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title