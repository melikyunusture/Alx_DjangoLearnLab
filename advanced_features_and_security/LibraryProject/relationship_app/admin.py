from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin interface for CustomUser model.
    """
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Unregister the default User model
admin.site.unregister(CustomUser)

# Register the custom User model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)