import requests
from django.shortcuts import render
from django.http import HttpResponse


def shoppingcart(request):
    activeUser = 2 #two users 1/2
    response = requests.get('http://localhost:8000/userdetail/'+str(activeUser)+"/")
    userInfo = response.json()
    cart = userInfo["cart"] #gets all cart info as list of dicts
   
    # bookQuantities = userInfo["cart"]["quantity"]
    # print(bookQuantities)
    # bookQlist = list()
    # for key in cart:
    #     for quantity in cart["quantity"]
    #     print(quantity)

    i=0
    for item in cart:
        response = requests.get('http://localhost:8000/detail/' + str(item['book']) + "/")
        book = response.json()
        cart[i]["book"] = book
        i += 1
 
    print(cart)
    return render(request, 'pages/shoppingcart.html', {"cartItems": cart})