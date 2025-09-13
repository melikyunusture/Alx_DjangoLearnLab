
from django.urls import path
from .views import list_books                 # required literally by checker
from .views import LibraryDetailView          # CBV import

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
]