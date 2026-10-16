from django.contrib import admin
from .models import Author , Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_year','rating' ,'is_available' , 'date_added')
    list_filter = ('genre', 'is_available', 'published_year')
    search_fields = ('title', 'author__name')   
    list_editable = ('is_available')