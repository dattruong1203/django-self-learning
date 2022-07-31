from django.contrib import admin
from .models import Genre, Book, Language, Author, BookInstance

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(BookInstance)
