from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
import requests
from .models import Wishlist

wishlists = [
    {
        'name': 'Fiction List',
        'user': 'Fabio',
        'books': [ {'Book1'}, {'Book2'}, {'book3'} ],
        'date_created': 'August 27, 2018'
    },
    {
        'name': 'Non-Fiction List',
        'user': 'Luis',
        'books': [ {'Book1', 'Book2', 'Book3'} ],
        'date_created': 'August 28, 2018'
    },
]


def wishlist(request):
    activeUser = 1
    response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    userInfo = response.json()
    wishlistList = userInfo['wishlist']

    userList = list()

    booksInWishlist = list()
    for item in wishlistList:
        response = requests.get('http://localhost:8000/detail/' + str(item["book"]) + "/")
        book = response.json()
        booksInWishlist.append(book)



    #content = {
     #   'wishlist': Wishlist.objects.all()
    #}
    return render(request, 'pages/wishlist.html', {"wishlistListItems": wishlistList, "books": booksInWishlist})


class WishlistListView(ListView):
    model = Wishlist
    template_name = 'pages/wishlist.html'
    context_object_name = 'wishlist'
    ordering = [ '-date_posted' ]


class WishlistDetailView(DetailView):
    template_name = 'pages/wishlist_form.html'
    model = Wishlist


class WishlistCreateView(CreateView):
    model = Wishlist
    template_name = 'pages/wishlist_create.html'
    fields = [ 'name' ]

    def test_func(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # activeUser = 1
    # response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
    # userInfo = response.json()
    # wishlist = userInfo["wishlist"]  # gets all cart info as list of dicts
    # print(wish)

    # booksInWishlist = list()
    # for item in wishlist:
    #   response = requests.get('http://localhost:8000/detail/' + str(item[ "wish1" ][ 0 ][ 'book' ]) + "/")
    #  book = response.json()
    # booksInWishlist.append(book)

    # for item in userInfo["wishlist"]:
    # book_ids = [entry['book'] for booklist in item.values() for entry in booklist]
    # print(book_ids)

    # return render(request, ', {"wishlistItems": wishlist, "books": booksInWishlist})
