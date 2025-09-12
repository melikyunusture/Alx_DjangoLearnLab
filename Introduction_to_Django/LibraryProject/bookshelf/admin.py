

from django.contrib import admin
from .models import Book

# Customize how Book appears in the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns displayed in the list view
    search_fields = ('title', 'author')                      # Enable search by title or author
    list_filter = ('publication_year',)                     # Add filter by publication year
    ordering = ('title',)                                   # Default ordering by title

# Register Book with the customized admin options
admin.site.register(Book, BookAdmin)

