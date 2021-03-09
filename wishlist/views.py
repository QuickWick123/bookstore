from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import WishlistItem


def wishlistView(request):
    all_wishlist_items = WishlistItem.objects.all()
    return render(request, 'pages/wishlist.html',
                  {'all_items': all_wishlist_items})

def addWishlist(request):
    new_item = WishlistItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/wishlist/')


def deleteWishlist(request, wishlist_id):
    item_to_delete = WishlistItem.objects.get(id=wishlist_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/wishlist/')
