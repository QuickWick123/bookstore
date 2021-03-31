from django.db import models


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
    rating = models.IntegerField()
    catetgory = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    publishDate = models.DateField()
    publisher = models.CharField(max_length=100)
    authorbio = models.CharField(max_length=1000)
    fullurl = models.CharField(max_length=200)


class UserProfiles(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=100)
    homeAddress = models.CharField(max_length=100)
    cart = models.JSONField(null=True)
    saveLater = models.JSONField(null=True)
    wishlist = models.JSONField(null=True)
    wishlistName = models.CharField(max_length=100, default="null")