import requests
from django.shortcuts import render
from django.http import HttpResponse

def shoppingcart(request):
    import requests
    from django.shortcuts import render
    from django.http import HttpResponse

    def shoppingcart(request):
        activeUser = 1
        response = requests.get('http://localhost:8000/userdetail/' + str(activeUser) + "/")
        userInfo = response.json()
        cart = userInfo["cart"]  # gets all cart info as list of dicts

        booksInCart = list()
        for item in cart:
            response = requests.get('http://localhost:8000/detail/' + str(item['book']) + "/")
            book = response.json()
            booksInCart.append(book)

        return render(request, 'pages/shoppingcart.html', {"cartItems": cart, "books": booksInCart})
    

