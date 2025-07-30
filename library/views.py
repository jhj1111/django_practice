from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    book_total_list = Book.objects.all()
    
    return render(request,
                  template_name='library/index.html',
                  context={'book_total' : book_total_list})
    
def detail(request, pk):
    book_single_list = Book.objects.get(pk=pk)
    
    return render(request,
                  template_name='library/detail.html',
                  context={'book_single' : book_single_list})