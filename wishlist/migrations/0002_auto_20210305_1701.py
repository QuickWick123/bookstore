# Generated by Django 3.1.5 on 2021-03-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='book',
            field=models.TextField(),
        ),
    ]