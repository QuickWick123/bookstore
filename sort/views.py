import requests
import json
from django.db.models import Q
from django.views.generic.list import ListView
from bookstore_api.models import Book
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator



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

TEMPLATE_NAME = "pages/sort.html"

class SearchResultsView(ListView):
   model = Book
   template_name = 'pages/searchResults.html'
   paginate_by = 3

   def get_queryset(self): # new
      query = self.request.GET.get('q')
      object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query)
        )
      return object_list

   def listing(self):
    books = Book.objects.all()
    paginator = Paginator(books, 2) # Show 25 contacts per page.

    page_number = self.request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(self.request, 'list.html', {'page_obj': page_obj})


def browse_results_view(request):
   book = Book.objects.all()
   return render(request, TEMPLATE_NAME, {'book': book})

def browse_by_category(request, catetgory):
   if catetgory is not None:
      result_list = Book.objects.filter(Q(catetgory__icontains=catetgory))
      return render(request, TEMPLATE_NAME,{'result_list':result_list})
   else:
      browse_results_view(request)

def top_10_seller(request):
   top_10_list = Book.objects.all()
   return render(request, TEMPLATE_NAME, {'top_10_list': top_10_list})

#  obj = requests.get('http://localhost:8000/book')
#    for category in obj: 
#       categories[category["categories"]] = category

# class BrowseResultsView(ListView):
#    model = Book
#    template_name = TEMPLATE_NAME
#    def get_queryset(self): # new
#      #query = self.request.GET.get('q')
#       query = self.request.GET.get('catetgory')
#       object_list = Book.objects.filter(
#             Q(catetgory__icontains=query))
#       return object_list
  
   # def get_queryset(self):
   #    query = query.self.request.GET.get('q')
   #    object_list = Book.objects.fitler(name__contains='')

#  if 'q' in request.GET:
#       q = request.GET['q']
#       searchResult= Book.objects.filter(name__icontains=q)
#     else:
#        searchResult= Book.objects.all()

def searchview(request):
   return render(request, 'pages/sort.html')