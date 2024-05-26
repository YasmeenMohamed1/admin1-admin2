from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import *

# Create your views here.

def list_books(request) :
    books = Book.objects.all()
    return render( request , 'book/list_books.html',context={'books':books})


def update_book(request , id) :
    return render( request , 'book/update_book.html',context={'id':id})

def delete_book(request , id) :
    Book.objects.filter(id=id).delete()
    return HttpResponseRedirect('/Book/list')

def details_of_books(request , name) :
    book = Book.objects.filter(name=name).first()

    return render(request,'book/book_details.html', context={'book':book})

