import requests
import json
from django.shortcuts import render
from django.http import HttpResponse


def shoppingcart(request):

    return render(request, 'pages/shoppingcart.html', {"cartItems": buildData(), "cartTotal": cartTotal()})


def deleteItem(request, book_id):
    activeUser = 1
    response = requests.delete('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id})
    print("resp", response)

    return shoppingcart(request)

def updateQuantity(request, book_id):
    activeUser = 1
    quantityButton = int(request.GET.get('q')) #returns form quantity
    response = requests.patch('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id, "quantity": quantityButton})

    print(quantityButton)
    return shoppingcart(request)

def buildData():
    activeUser = 1 #two users 1/2
    response = requests.get('http://localhost:8000/userdetail/'+str(activeUser)+"/")
    userInfo = response.json()
    cart = userInfo["cart"] 

    i=0
    for item in cart:
        response = requests.get('http://localhost:8000/detail/' + str(item['book']) + "/")
        book = response.json()
        cart[i]["book"] = book
        i += 1
    return cart

def cartTotal():
    activeUser = 1 #two users 1/2
    response = requests.get('http://localhost:8000/userdetail/'+str(activeUser)+"/")
    userInfo = response.json()
    cart = userInfo["cart"] 

    i = 0
    total = 0
    for item in cart:
        response = requests.get('http://localhost:8000/detail/' + str(item['book']) + "/")
        book = response.json()
        item = int(book['price'])
        quantity = int(cart[i]["quantity"])
        subTotal = item*quantity
        total = subTotal + total
        i += 1
        cartTotalFormatted = "{:.2f}".format(total)
        
    return cartTotalFormatted