from django.contrib import admin
from .models import Author , Book

@admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')

@admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_year', 'is_available')
    list_filter = ('genre', 'is_available', 'published_year')
    search_fields = ('title', 'author__name')   