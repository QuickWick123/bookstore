from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=100, default='none')
    language = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.title
