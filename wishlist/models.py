from django.db import models


# Create your models here

class WishlistItem(models.Model):
    content = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.IntegerField()
    pageCount = models.IntegerField()
    publishedDate = models.JSONField()
    thumbnailUrl = models.URLField()
    shortDescription = models.CharField(max_length=1000)
    longDescription = models.CharField(max_length=3000)
    status = models.CharField(max_length=100)
    authors = models.JSONField()
    categories = models.JSONField()
    price = models.FloatField(null=True)
