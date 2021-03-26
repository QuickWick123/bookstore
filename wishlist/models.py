from django.db import models
from django.utils import timezone


# Create your models here
class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    Book = models.JSONField(null=True)
    User = models.JSONField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
