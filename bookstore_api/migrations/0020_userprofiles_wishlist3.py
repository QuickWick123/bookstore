# Generated by Django 3.1.5 on 2021-04-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0019_userprofiles_wishlist2name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wishlist3',
            field=models.JSONField(null=True),
        ),
    ]