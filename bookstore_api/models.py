from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.IntegerField()
    pageCount = models.IntegerField(db_column='pageCount')
    publishedDate = models.JSONField(db_column='publishedDate')
    thumbnailUrl = models.URLField(db_column='thumbnailUrl', max_length=200)
    shortDescription = models.CharField(db_column='shortDescription', max_length=1000)
    longDescription = models.CharField(db_column='longDescription', max_length=3000)
    status = models.CharField(max_length=100)
    authors = models.JSONField()
    categories = models.JSONField()
    price = models.FloatField(blank=True, null=True)
    rating = models.IntegerField()
    catetgory = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    publishDate = models.DateField()

class UserProfiles(models.Model):
    userName = models.CharField(db_column='userName', max_length=100)
    password = models.CharField(max_length=100)
    firstName = models.CharField(db_column='firstName', max_length=100)
    lastName = models.CharField(db_column='lastName', max_length=100)
    emailAddress = models.CharField(db_column='emailAddress', max_length=100)
    homeAddress = models.CharField(db_column='homeAddress', max_length=100)
    cart = models.JSONField(blank=True, null=True)
    saveLater = models.JSONField(db_column='saveLater', blank=True, null=True)
    