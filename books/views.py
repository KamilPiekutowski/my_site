from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# \books\views.py
def search_form(request):
    return render(request,'books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        #print("q contains %s" % q)
        if not q:
            errors.append("Your search box is empty.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books' : books, 'query': q })
    return render(request,'books/search_form.html', {'errors' : errors})


