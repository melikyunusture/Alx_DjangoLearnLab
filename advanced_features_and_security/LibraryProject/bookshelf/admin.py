

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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Unregister the default User model
#admin.site.unregister(CustomUser)

# Register the custom User model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)



'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Unregister the default User model
admin.site.unregister(CustomUser)

# Register the custom User model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

'''