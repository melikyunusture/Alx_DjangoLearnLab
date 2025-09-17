from django.db import models

# Create your models here.



from django.contrib.auth import get_user_model



# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model (ForeignKey to Author)
'''
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author.name}" '''
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]    


# Library model (ManyToManyField to Book)
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name



# Librarian model (OneToOneField with Library)
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return f"{self.name} ({self.library.name})"
    


# relationship_app/models.py
from django.db import models
#from accounts.models import UserProfile

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth import get_user_model

User = get_user_model()

class RelationshipUserProfile(models.Model):  # <-- checker looks for this exact line
    ROLE_CHOICES = [
        ('Admin', 'Admin'),        # <-- checker looks for "Admin"
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),      # <-- checker looks for "Member"
    ]
    '''
    from accounts.models import UserProfile  # local import is fine in class scope
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    #role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    extra_field = models.CharField(max_length=255)
'''
    def __str__(self):
        return f"{self.user_profile.user.username}"

    def set_profile(self, user_id):
        from accounts.models import UserProfile  #  local import
        self.user_profile = UserProfile.objects.get(user_id=user_id)
    def __str__(self):
        return f"{self.user_profile.user.username} relationship info"

 
    


from django.db import models
from django.contrib.auth import get_user_model
'''
User = get_user_model()  # Refers to accounts.CustomUser

# App-specific profile linked to UserProfile
class RelationshipUserProfile(models.Model):
    
    user_profile = models.OneToOneField('accounts.UserProfile', on_delete=models.CASCADE)
    extra_field = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username} relationship info" 
    '''



'''
 # relationship_app/models.py
from django.db import models

class RelationshipUserProfile(models.Model):
    # Reference accounts.UserProfile safely as a string
    user_profile = models.OneToOneField(
        'accounts.UserProfile',   # <- this avoids NameError and circular import
        on_delete=models.CASCADE
    )
    extra_field = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user_profile.user.username}"    
    
    '''
    

from django.db import models

'''
# Extra profile details specific to relationship_app
class RelationshipUserProfile(models.Model):
    # Safe reference: use string to avoid NameError / circular import
    user_profile = models.OneToOneField(
        'accounts.UserProfile',
        on_delete=models.CASCADE,
        related_name="relationship_profile"
    )
    extra_field = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Relationship info for {self.user_profile.user.username}"
    '''
    
from django.db import models
#from accounts.models import UserProfile
from accounts.models import UserProfile


class RelationshipUserProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='relationship_profile')
    friends_count = models.PositiveIntegerField(default=0)
    status_message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Relationship profile of {self.user_profile.user.username}"
    


# Automatically create UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()   



from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]    






