import requests
import json
from django.db.models import Q
from django.views.generic.list import ListView
from bookstore_api.models import Book
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator



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

   # def listing(self):
   #  books = Book.objects.all()
   #  paginator = Paginator(books, 2) # Show 25 contacts per page.
   #  page_number = self.request.GET.get('page')
   #  page_obj = paginator.get_page(page_number)
   #  return render(self.request, 'list.html', {'page_obj': page_obj})

def searchview(request):
   return render(request, 'pages/sort.html')

def browse_results_view(request):
   book = Book.objects.all()
   return render(request, TEMPLATE_NAME, {'book': book})

def browse_by_category(request, catetgory):
   if catetgory is not None:
      result_list = Book.objects.filter(Q(catetgory__icontains=catetgory))
      return render(request, TEMPLATE_NAME,{'result_list':result_list})
   else:
      browse_results_view(request)

def top_10_sellers(request):
   top_10_list = Book.objects.all()
   return render(request, TEMPLATE_NAME, {'top_10_list': top_10_list})


def top_20_sellers(request, page=None):
   top_20_list = Book.objects.all()
   top_20_list_paginator = Paginator(top_20_list, 10) # Show 25 contacts per page.
   page_num = request.GET.get(page)
   page = top_20_list_paginator.get_page(page_num)
   context = {
      'count' : top_20_list_paginator.count,
      'page' : page
   }
   return render(request, TEMPLATE_NAME, context)

def rating5(request):
      rating5_book_list = Book.objects.filter(Q(rating__icontains=5))
      return render(request, TEMPLATE_NAME, {'rating5_book_list': rating5_book_list})

def rating4(request):
      rating4_book_list = Book.objects.filter(Q(rating__icontains=4))
      return render(request, TEMPLATE_NAME, {'rating4_book_list': rating4_book_list})

def rating3(request):
      rating3_book_list = Book.objects.filter(Q(rating__icontains=3))
      return render(request, TEMPLATE_NAME, {'rating3_book_list': rating3_book_list})

def rating2(request):
      rating2_book_list = Book.objects.filter(Q(rating__icontains=2))
      return render(request, TEMPLATE_NAME, {'rating2_book_list': rating2_book_list})

def rating1(request):
      rating1_book_list = Book.objects.filter(Q(rating__icontains=1))
      return render(request, TEMPLATE_NAME, {'rating1_book_list': rating1_book_list})

