import requests
from django.db.models import Q
from django.views.generic.list import ListView
from bookstore_api.models import Book
from django.shortcuts import render
from django.http import HttpResponse



# def sort(request):
#    #   return render(request, 'pages/sort.html')
#     response = requests.get('http://localhost:8000/book')
#     books = Book.objects
#     return render(request, 'pages/sort.html', {"books": books})

# def get_queryset(request):
#    query = request.get('http://localhost:8000/book')
#    results = Book.objects.filter(
#       Q(title__icontains=query) | Q(authors__icontains=query)
#       )
  
#    return render(request, 'pages/sort.html', {'results': results})


class SearchResultsView(ListView):
   model = Book
   template_name = 'pages/sort.html'

   def get_queryset(self): # new
      query = self.request.GET.get('q')
      object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query)
        )
      return object_list

   # def get_queryset(self):
   #    query = query.self.request.GET.get('q')
   #    object_list = Book.objects.fitler(name__contains='')

#  if 'q' in request.GET:
#       q = request.GET['q']
#       searchResult= Book.objects.filter(name__icontains=q)
#     else:
#        searchResult= Book.objects.all()