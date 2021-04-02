import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from bookstore_api.models import UserProfiles
from .forms import CreateWishForm

activeUser = 1


def wishlist(request):
    response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    users = response.json()
    return render(request, 'pages/wishlist.html', {"wishlistItems": wishlistView(), 'users': users, "wishlistItems2":wishlistView2(), "wishlistItems3": wishlistView3()})


def wishlistView():
    response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    userInfo = response.json()
    wishlists = userInfo[ 'wishlist']

    i = 0
    # booksInWishlist = list()
    for item in wishlists:
        response = requests.get('http://localhost:8000/detail/' + str(item[ "book" ]) + "/")
        book = response.json()
        # booksInWishlist.append(book)
        wishlists[ i ][ "book" ] = book
        i += 1
    # return booksInWishlist
    return wishlists

def wishlistView2():
    response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    userInfo = response.json()
    wishlist2 = userInfo[ 'wishlist2']

    i = 0
    # booksInWishlist = list()
    for item in wishlist2:
        response = requests.get('http://localhost:8000/detail/' + str(item[ "book" ]) + "/")
        book = response.json()
        # booksInWishlist.append(book)
        wishlist2[ i ][ "book" ] = book
        i += 1
    # return booksInWishlist
    return wishlist2

def wishlistView3():
    response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    userInfo = response.json()
    wishlist3 = userInfo[ 'wishlist3']

    i = 0
    # booksInWishlist = list()
    for item in wishlist3:
        response = requests.get('http://localhost:8000/detail/' + str(item[ "book" ]) + "/")
        book = response.json()
        # booksInWishlist.append(book)
        wishlist3[ i ][ "book" ] = book
        i += 1
    # return booksInWishlist
    return wishlist3

def deleteItem(request, book_id):
    response = requests.delete('http://localhost:8000/userwish/' + str(activeUser) + "/", data={"book": book_id})
    print("resp", response)

    return wishlist(request)

def deleteItem2(request, book_id):
    response = requests.delete('http://localhost:8000/userwish2/' + str(activeUser) + "/", data={"book": book_id})
    print("resp", response)
    return wishlist(request)

def deleteItem3(request, book_id):

    response = requests.delete('http://localhost:8000/userwish3/' + str(activeUser) + "/", data={"book": book_id})

    return wishlist(request)

def addCart(request, book_id):

    response = requests.delete('http://localhost:8000/userwish/' + str(activeUser) + "/", data={"book": book_id})
    response = requests.post('http://localhost:8000/usercart/' + str(activeUser) + "/", data={"book": book_id})

    return wishlist(request)

def addCart2(request, book_id):

    response = requests.delete('http://localhost:8000/userwish2/' + str(activeUser) + "/", data={"book": book_id})
    response = requests.post('http://localhost:8000/usercart/' + str(activeUser) + "/", data={"book": book_id})

    return wishlist(request)

def addCart3(request, book_id):

    response = requests.delete('http://localhost:8000/userwish3/' + str(activeUser) + "/", data={"book": book_id})
    response = requests.post('http://localhost:8000/usercart/' + str(activeUser) + "/", data={"book": book_id})

    return wishlist(request)

def add(request):
    if request.method == "POST" or None:
        form = CreateWishForm(request.POST or None)
        if form.is_valid():
            UserProfiles.wishlistName = form.cleaned_data
            form.save()
            return render(request, 'pages/wishlist_create.html', {'form': form})
        else:
            form = CreateWishForm
            return render(request, 'pages/wishlist_create.html', {'form': form})
    else:
        form = CreateWishForm
        return render(request, 'pages/wishlist_create.html', {'form': form})

# def updateName(request, book_id):
# updateButton = str(request.GET.get('name'))
# response = requests.patch('http://localhost:8000/usercart/' + str(activeUser) + "/",
# data={"book": book_id, "quantity": quantityButton})
