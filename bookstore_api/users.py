from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfiles
from .serializers import UserSerializer


class UserGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                         mixins.CreateModelMixin, mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = UserProfiles.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)


class UsersAPIView(APIView):

    def get(self, request):
        users = UserProfiles.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDetails(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status= status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        UserProfiles = self.get_object(id)
        serializer = UserSerializer(UserProfiles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        UserProfiles = self.get_object(id)
        UserProfiles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#NEW CLASS FOR CART API's POST & DELETE
class userCart(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status= status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        
        user = self.get_object(id)
        bookData = request.data
        bookId = bookData["book"]
        defaultValue = 1
        cart = user.cart
        newItem = {}
        newItem.update({"book": bookId})
        if "quantity" not in newItem:
            newItem['quantity'] = 1
       
        cart.append(newItem)
        user.cart = cart
        user.save()
        return Response(user.cart, status = status.HTTP_200_OK)


    def delete(self, request, id):

        user = self.get_object(id)
        removeIndex = request.data
        oldCart = user.cart
        for i, dic in enumerate(oldCart):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldCart.pop(i)
                user.cart = oldCart
                user.save()
                return Response(user.cart, status = status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):

        user = self.get_object(id)
        cart = user.cart
        updateDic = request.data
        # print(updateDic)
        # print(cart)
        # print(updateDic["quantity"])

        for i, dic in enumerate(cart):
            print(type(dic["book"]), "=", type(updateDic["book"]))
            if int(dic["book"]) == int(updateDic["book"]):
                dic["quantity"] = updateDic["quantity"]
                user.save()
                print("SUCCESS!!")
                return Response(user.cart, status = status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

#NEW CLASS FOR SAVE FOR LATER

class userSaveLater(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status= status.HTTP_204_NO_CONTENT)


    def post(self, request, id): #Posts item to save for later list
        
        user = self.get_object(id)
        newItem = request.data
        laterCart = user.saveLater
        laterCart.append(newItem)
        user.saveLater = laterCart
        user.save()
        return Response(user.saveLater, status = status.HTTP_200_OK)

    def delete(self, request, id):#deletes item from save for later list

        user = self.get_object(id)
        removeIndex = request.data
        oldLater = user.saveLater
        for i, dic in enumerate(oldLater):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldLater.pop(i)
                user.saveLater = oldLater
                user.save()
                return Response(user.saveLater, status = status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

class userWish(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, id):
        user = self.get_object(id)
        newItem = request.data
        wishlist = user.wishlist
        wishlist.append(newItem)
        user.wishlist = wishlist
        user.save()
        return Response(user.wishlist, status=status.HTTP_200_OK)

    def delete(self, request, id):

        user = self.get_object(id)
        removeIndex = request.data
        oldWish = user.wishlist
        for i, dic in enumerate(oldWish):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldWish.pop(i)
                print(oldWish)
                user.wishlist = oldWish
                user.save()
                print("complete")
                return Response(user.wishlist, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)


class userWish2(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, id):
        user = self.get_object(id)
        newItem = request.data
        wishlist2 = user.wishlist2
        wishlist2.append(newItem)
        user.wishlist2 = wishlist2
        user.save()
        return Response(user.wishlist2, status=status.HTTP_200_OK)

    def delete(self, request, id):

        user = self.get_object(id)
        removeIndex = request.data
        oldWish2 = user.wishlist2
        for i, dic in enumerate(oldWish2):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldWish2.pop(i)
                user.wishlist2 = oldWish2
                user.save()
                return Response(user.saveLater, status = status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
class userWish3(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, id):
        user = self.get_object(id)
        newItem = request.data
        wishlist3 = user.wishlist3
        wishlist3.append(newItem)
        user.wishlist3 = wishlist3
        user.save()
        return Response(user.wishlist3, status=status.HTTP_200_OK)

    def delete(self, request, id):

        user = self.get_object(id)
        removeIndex = request.data
        oldWish3 = user.wishlist3
        for i, dic in enumerate(oldWish3):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldWish3.pop(i)
                user.wishlist3 = oldWish3
                user.save()
                return Response(user.saveLater, status = status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

class userWishToCart(APIView):

    def get_object(self, id):
        try:
            return UserProfiles.objects.get(id=id)

        except UserProfiles.DoesNotExist:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request, id):
        user = self.get_object(id)
        newItem = request.data
        wishlist = user.wishlist
        wishlist.append(newItem)
        user.wishlist = wishlist
        user.save()
        return Response(user.wishlist, status=status.HTTP_200_OK)

    def delete(self, request, id):

        user = self.get_object(id)
        removeIndex = request.data
        oldWish = user.wishlist
        for i, dic in enumerate(oldWish):
            print(type(dic["book"]), "=", type(removeIndex["book"]))
            if int(dic["book"]) == int(removeIndex["book"]):
                oldWish.pop(i)
                print(oldWish)
                user.wishlist = oldWish
                user.save()
                print("complete")
                return Response(user.wishlist, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
