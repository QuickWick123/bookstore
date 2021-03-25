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
    publisher = models.CharField(max_length=100, blank=True, null=True)
    authorbio = models.CharField(max_length=1000, blank=True, null=True)
    orderid = models.ForeignKey('Orderplaced', models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    cartid = models.ForeignKey('Cart', models.DO_NOTHING, db_column='cartid', blank=True, null=True)
    commentsid = models.ForeignKey('Comments', models.DO_NOTHING, db_column='commentsid', blank=True, null=True)


class UserProfiles(models.Model):
    userName = models.CharField(db_column='userName', max_length=100)
    password = models.CharField(max_length=100)
    firstName = models.CharField(db_column='firstName', max_length=100)
    lastName = models.CharField(db_column='lastName', max_length=100)
    emailAddress = models.CharField(db_column='emailAddress', max_length=100)
    homeAddress = models.CharField(db_column='homeAddress', max_length=100)
    cart = models.JSONField(blank=True, null=True)
    saveLater = models.JSONField(db_column='saveLater', blank=True, null=True)
    homeaddress2 = models.CharField(max_length=100, blank=True, null=True)
    homeaddress3 = models.CharField(max_length=100, blank=True, null=True)
    shipaddress = models.CharField(max_length=100, blank=True, null=True)
    phoneno = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    creditcard = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    wishlistid = models.ForeignKey('Wishlist', models.DO_NOTHING, db_column='wishlistid', blank=True, null=True)
    commentsid = models.ForeignKey('Comments', models.DO_NOTHING, db_column='commentsid', blank=True, null=True)
    cartid = models.ForeignKey('Cart', models.DO_NOTHING, db_column='cartid', blank=True, null=True)
    #actualid = models.IntegerField(primary_key=True)


class Cart(models.Model):
    cartid = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    totalprice = models.FloatField(blank=True, null=True)
    actualid = models.ForeignKey(UserProfiles, models.DO_NOTHING, db_column='actualid', blank=True, null=True, related_name='actual_id')
    orderid = models.ForeignKey('Orderplaced', models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bookid', blank=True, null=True)
    latercartid = models.ForeignKey('Latercart', models.DO_NOTHING, db_column='latercartid', blank=True, null=True)



class Comments(models.Model):
    commentsid = models.IntegerField(primary_key=True)
    commentsactual = models.CharField(max_length=600, blank=True, null=True)
    actualid = models.ForeignKey(UserProfiles, models.DO_NOTHING, db_column='actualid', blank=True, null=True)
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bookid', blank=True, null=True)



class Latercart(models.Model):
    latercartid = models.IntegerField(primary_key=True)
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='cartid', blank=True, null=True)



class Orderplaced(models.Model):
    orderid = models.IntegerField(primary_key=True)
    totalprice = models.FloatField(blank=True, null=True)
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='cartid', blank=True, null=True)


class Wishlist(models.Model):
    wishlistid = models.IntegerField(primary_key=True)
    wishlistname = models.CharField(max_length=40, blank=True, null=True)
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bookid', blank=True, null=True)
    actualid = models.ForeignKey(UserProfiles, models.DO_NOTHING, db_column='actualid', blank=True, null=True)
