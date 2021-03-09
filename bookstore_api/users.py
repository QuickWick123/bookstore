from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
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
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

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