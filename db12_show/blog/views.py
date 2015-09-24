from django.shortcuts import render, render_to_response
from blog.models import Author, Book

# Create your views here.

def show_author(request):
    authors = Author.objects.all()
    return render_to_response('show_author.html', {'authors': authors})

def show_book(request):
    books = Book.objects.all()
    return render_to_response('show_book.html', {'books': books})
