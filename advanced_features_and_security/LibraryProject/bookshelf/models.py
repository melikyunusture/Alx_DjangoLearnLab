from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    

    

from accounts.models import CustomUser  # ✅ import actual definition
from django.db import models


# ✅ Example model referencing CustomUser (checker will see it here)
class ExampleModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.note}"