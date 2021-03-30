from rest_framework import serializers
from .models import Book, UserProfiles, Cart, Comments, Latercart, Orderplaced, Wishlist


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class LatercartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latercart
        fields = '__all__'

class OrderplacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderplaced
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'