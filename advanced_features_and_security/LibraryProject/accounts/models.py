from django.db import models

# Create your models here.from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#from relationship_app.models import RelationshipUserProfile 
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

#User = get_user_model()  # <- safe reference to your CustomUser
class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser"""

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(username, email, password, **extra_fields)

'''
class CustomUser(AbstractUser):
    """Custom user model extending Django’s AbstractUser"""


    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username '''
    
    



'''

# accounts/models.py


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

AUTH_USER_MODEL = 'accounts.CustomUser'


    # accounts/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
   # bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)


    def __str__(self):
        return self.user.username


'''




    

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Custom User model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.username


# Profile linked to CustomUser
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
    


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"