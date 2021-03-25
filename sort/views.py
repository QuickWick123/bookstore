import requests
import json
from django.db.models import Q
from django.views.generic.list import ListView
from bookstore_api.models import Book
from django.shortcuts import render, redirect
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
   query = request.GET.get('sort_filed')
   if query is not None:
      result_list = Book.objects.filter(Q(catetgory__icontains=catetgory))
      result_list = sort(request, result_list)
      return render(request, TEMPLATE_NAME,{'result_list':result_list})
   else:
      result_list = Book.objects.filter(Q(catetgory__icontains=catetgory))
      return render(request, TEMPLATE_NAME,{'result_list':result_list})

def top_10_sellers(request):
      query = request.GET.get('sort_filed')
      if query is not None:
         top_10_list = Book.objects.all()
         top_10_list = sort(request, top_10_list)
         return render(request, TEMPLATE_NAME, {'top_10_list': top_10_list})
      else:
         top_10_list = Book.objects.all()
         return render(request, TEMPLATE_NAME, {'top_10_list': top_10_list})


def top_20_sellers(request, page=None):
   top_20_list = Book.objects.all()
   query = request.GET.get('sort_filed')
   if query is not None:
      top_20_list = sort(request, top_20_list)
      top_20_list_paginator = Paginator(top_20_list, 10) # Show 25 contacts per page.
      page_num = request.GET.get(page)
      page = top_20_list_paginator.get_page(page_num)
      context = {
         'count' : top_20_list_paginator.count,
         'page' : page
      }
      return render(request, TEMPLATE_NAME, context)
   else:
      top_20_list_paginator = Paginator(top_20_list, 10) # Show 25 contacts per page.
      page_num = request.GET.get(page)
      page = top_20_list_paginator.get_page(page_num)
      context = {
         'count' : top_20_list_paginator.count,
         'page' : page
      }
      return render(request, TEMPLATE_NAME, context)

def rating5(request):
      query = request.GET.get('sort_filed')
      if query is not None:
         rating5_book_list = Book.objects.filter(Q(rating__icontains=5))
         rating5_book_list = sort(request, rating5_book_list)
         return render(request, TEMPLATE_NAME, {'rating5_book_list': rating5_book_list})
      else:
         rating5_book_list = Book.objects.filter(Q(rating__icontains=5))
         return render(request, TEMPLATE_NAME, {'rating5_book_list': rating5_book_list})

def rating4(request):
      query = request.GET.get('sort_filed')
      if query is not None:
         rating4_book_list = Book.objects.filter(Q(rating__icontains=4))
         rating4_book_list = sort(request, rating4_book_list)
         return render(request, TEMPLATE_NAME, {'rating4_book_list': rating4_book_list})
      else:
         rating4_book_list = Book.objects.filter(Q(rating__icontains=4))
         return render(request, TEMPLATE_NAME, {'rating4_book_list': rating4_book_list})

def rating3(request):
      query = request.GET.get('sort_filed')
      if query is not None:
         rating3_book_list = Book.objects.filter(Q(rating__icontains=3))
         rating3_book_list = sort(request, rating3_book_list)
         return render(request, TEMPLATE_NAME, {'rating3_book_list': rating3_book_list})
      else: 
         rating3_book_list = Book.objects.filter(Q(rating__icontains=3))
         return render(request, TEMPLATE_NAME, {'rating3_book_list': rating3_book_list})

def rating2(request):
      query = request.GET.get('sort_filed')
      if query is not None:
         rating2_book_list = Book.objects.filter(Q(rating__icontains=2))
         rating2_book_list = sort(request, rating2_book_list)
         return render(request, TEMPLATE_NAME, {'rating2_book_list': rating2_book_list})
      else:
         rating2_book_list = Book.objects.filter(Q(rating__icontains=2))
         return render(request, TEMPLATE_NAME, {'rating2_book_list': rating2_book_list})

def rating1(request):
   query = request.GET.get('sort_filed')
   if query is not None:
      rating1_book_list = Book.objects.filter(Q(rating__icontains=1))
      rating1_book_list = sort(request, rating1_book_list)
      return render(request, TEMPLATE_NAME, {'rating1_book_list': rating1_book_list})
   else:
      rating1_book_list = Book.objects.filter(Q(rating__icontains=1))
      return render(request, TEMPLATE_NAME, {'rating1_book_list': rating1_book_list})


def sort(request, model):
   query = request.GET.get('sort_filed')
   sort_list = model
   if query is not None:
      if query == "title_a-z":
         sort_list = sort_list.order_by('title')
         return sort_list
      elif query == 'author': 
         sort_list = sort_list.order_by('-authors')
         return sort_list
      elif query == 'price_low_to_high':
         sort_list = sort_list.order_by('price')
         return sort_list
      elif query == 'price_high_to_low':
         sort_list = sort_list.order_by('-price')
         return sort_list
      elif query == 'rating_low_to_high':
         sort_list = sort_list.order_by('rating')
         return sort_list
      elif query == 'rating_high_to_low':
         sort_list = sort_list.order_by('-rating')
         return sort_list
      elif query == 'release_date':
         sort_list = sort_list.order_by('-publishedDate')
         return sort_list
   else:
      return render(request, TEMPLATE_NAME, {'sort_list': sort_list})

      