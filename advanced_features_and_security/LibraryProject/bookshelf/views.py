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



'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# ---- Create Book ----
# Only users with the 'can_create' permission can access this view
@permission_required('relationship_app.can_create')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

# ---- Edit Book ----
# Only users with the 'can_edit' permission can access this view
@permission_required('relationship_app.can_edit')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# ---- Delete Book ----
# Only users with the 'can_delete' permission can access this view
@permission_required('relationship_app.can_delete')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


'''


'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# ---- Book List ----
# This view lists all books and is protected by the 'can_view' permission.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ---- Create Book ----
# Only users with the 'can_create' permission can access this view.
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'bookshelf/add_book.html', {'authors': authors})

# ---- Edit Book ----
# Only users with the 'can_edit' permission can access this view.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'bookshelf/edit_book.html', {'book': book, 'authors': authors})

# ---- Delete Book ----
# Only users with the 'can_delete' permission can access this view.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_protect

# ---- Book List ----
# This view lists all books and is protected by the 'can_view' permission.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ---- Create Book ----
# Only users with the 'can_create' permission can access this view.
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        # Safely handle user input using ORM
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'bookshelf/add_book.html', {'authors': authors})

# ---- Edit Book ----
# Only users with the 'can_edit' permission can access this view.
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Safely handle user input using ORM
        book.title = request.POST.get('title')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'bookshelf/edit_book.html', {'book': book, 'authors': authors})

# ---- Delete Book ----
# Only users with the 'can_delete' permission can access this view.
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

# ---- Registration View ----
@csrf_protect
def register(request):
    if request.method == 'POST':
        # Use Django's built-in forms for secure input validation
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})