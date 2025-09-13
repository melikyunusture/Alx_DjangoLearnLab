from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Add filters on the right sidebar
    list_filter = ('publication_year',)

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)