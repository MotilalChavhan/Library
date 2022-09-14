from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 

    def __str__(self):
        return self.email

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    book_description = models.TextField(null=True)
    isbn = models.CharField(max_length=128)
    pages = models.CharField(max_length=128)

    def __str__(self):
        return self.book_title