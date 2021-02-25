from rest_framework import serializers
from .models import Book, UserProfiles


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = ['userName', 'password', 'firstName', 'lastName', 'emailAddress', 'homeAddress']