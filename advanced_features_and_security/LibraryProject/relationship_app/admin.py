from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RelationshipUserProfile


@admin.register(RelationshipUserProfile)
class RelationshipUserProfileAdmin(admin.ModelAdmin):
    list_display = ("user_profile", "friends_count", "status_message")
    search_fields = ("user_profile__user__username", "status_message")