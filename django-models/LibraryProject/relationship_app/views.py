from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book
from django.views import View

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view to show book details

from django.views.generic import DetailView
from .models import Library

# Class-based view to show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  # The object passed to the template

    