# Generated by Django 3.1.5 on 2021-03-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0008_userprofiles_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='date_created',
        ),
    ]
