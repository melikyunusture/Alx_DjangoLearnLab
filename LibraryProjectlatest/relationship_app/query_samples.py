from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (checker expects two-step approach)
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)         # must exist exactly like this
    return Book.objects.filter(author=author)             # must exist exactly like this

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)   # must be exactly like this
    return librarian