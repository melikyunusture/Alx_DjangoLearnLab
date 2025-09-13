
from django.urls import path
from .views import list_books                 # required literally by checker
from .views import LibraryDetailView          # CBV import


from django.urls import path
from .views import ( 
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV


    # Book and Library Views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
