# Generated by Django 3.1.5 on 2021-04-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0020_userprofiles_wishlist3'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wishlist3Name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]