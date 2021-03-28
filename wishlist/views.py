import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm


def wishlist(request):
    return render(request, 'pages/wishlist.html', {"wishlistItems": wishlistView()})


def wishlistView():
    response = requests.get('http://localhost:8000/userdetail/' + str(1) + "/")
    userInfo = response.json()
    wishlist = userInfo['wishlist']

    i = 0
    # booksInWishlist = list()
    for item in wishlist:
        response = requests.get('http://localhost:8000/detail/' + str(item["book"]) + "/")
        book = response.json()
        # booksInWishlist.append(book)
        wishlist[i]["book"] = book
        i += 1
    # return booksInWishlist
    return wishlist


def deleteItem(request, book_id):
    activeUser = 1
    response = requests.delete('http://localhost:8000/userwish/' + str(activeUser) + "/", data={"book": book_id})
    print("resp", response)

    return wishlist(request)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'pages/wishlist_create.html', {'form': form})
