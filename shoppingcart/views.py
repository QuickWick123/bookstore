import requests
import json
from django.shortcuts import render
from django.http import HttpResponse

def shoppingcart(request): #Main function. Displays all on page

    return render(request, 'pages/shoppingcart.html', {"cartItems": buildData(), "cartTotal": cartTotal(), "laterItems": LaterData()})

def postCart(request, book_id):
    activeUser = 1 #two users 1/2
    response = requests.post('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id})

    return shoppingcart(request)

def deleteItem(request, book_id): #delete cart item
    activeUser = 1 #two users 1/2
    response = requests.delete('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id})

    return shoppingcart(request)

def updateQuantity(request, book_id):
    activeUser = 1
    quantityButton = int(request.GET.get('q')) #returns form quantity
    response = requests.patch('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id, "quantity": quantityButton})

    return shoppingcart(request)

def buildData():
    activeUser = 1 
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

#SAVE FOR LATER FUNCTION AND VIEWS

def LaterData():
    activeUser = 1 #two users 1/2
    response = requests.get('http://localhost:8000/userdetail/'+str(activeUser)+"/")
    userInfo = response.json()
    laterList = userInfo["saveLater"] 

    i=0
    for item in laterList:
        response = requests.get('http://localhost:8000/detail/' + str(item["book"]) + "/")
        book = response.json()
        laterList[i]["book"] = book
        i += 1
    return laterList

def deleteLaterItem(request, book_id):
    activeUser = 1
    response = requests.delete('http://localhost:8000/latercart/'+str(activeUser)+"/", data = {"book": book_id})

    return shoppingcart(request)

def saveLaterItem(request, book_id):
    activeUser = 1
    response = requests.post('http://localhost:8000/latercart/'+str(activeUser)+"/", data = {"book": book_id})
    response = requests.delete('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id})

    return shoppingcart(request)

#WORK IN PROGRESS EDITED 3/29
def laterToCart(request, book_id):
    activeUser = 1
    print(book_id)
    response = requests.post('http://localhost:8000/usercart/'+str(activeUser)+"/", data = {"book": book_id})
    response = requests.delete('http://localhost:8000/latercart/'+str(activeUser)+"/", data = {"book": book_id})

    return shoppingcart(request)

def cartTotal():
    activeUser = 1 #two users 1/2
    response = requests.get('http://localhost:8000/userdetail/'+str(activeUser)+"/")
    userInfo = response.json()
    cart = userInfo["cart"] 
    i = 0
    total = 0

    if len(cart) == 0:
        cartTotalFormatted = 0

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