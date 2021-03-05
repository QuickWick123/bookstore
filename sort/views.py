import requests
from bookstore_api.models import Book
from django.shortcuts import render
from django.http import HttpResponse



def sort(request):
   #   return render(request, 'pages/sort.html')
    response = requests.get('http://localhost:5000/book')
    books = Book.objects
    
    if 'q' in request.GET:
      q = request.GET['q']
      searchResult= Book.objects.filter(name__icontains=q)
    else:
       searchResult= Book.objects.all()
    return render(request, 'pages/sort.html', {"books": books})



# class SearchResult(ListView):
#    model = Book
#    template_name = 'pages/sort.html'

#    def get_queryset(self):
#       query = query.self.request.GET.get('q')
#       object_list = Book.objects.fitler(name__contains='')
