from django.shortcuts import render ,redirect
import bcrypt
from django.shortcuts import *
from .models import *
# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context={
        'books':Books.objects.all(),
    }
    return render(request,"books.html",context)
def authors(request):
    context={
        'authors':Authors.objects.all(),
    }
    return render(request,"author.html",context)

def add_author(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        notes=request.POST['notes']
        new_author=Authors.objects.create(first_name=first_name,last_name=last_name,notes=notes)
        new_author.save()
        return redirect('/authors')

def view_author(request,id):
    context={
        'Authors':Authors.objects.all(),
        'author':Authors.objects.get(id=id),
        'books':Books.objects.all(),
        'book':Authors.objects.get(id=id).Books.all(),
    }
    return render(request,"author_info.html",context)

def append_author(request,id):
    option = Authors.objects.get(id = request.POST['books_author'])
    Books.objects.get(id =id).uploaded_by.add(option)
    
    return redirect(f'/view_author/{id}')

def append_book(request,id):
    option = Authors.objects.get(id = request.POST['authors_book'])
    Books.objects.get(id =id).uploaded_by.add(option)
    
    return redirect(f'/view_author/{id}')

def add_book(request):
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        new_book=Books.objects.create(title=title,description=description)
        new_book.save()
        return redirect('/')
def view_book(request,id):
    context={
        'books':Books.objects.all(),
        'book':Books.objects.get(id=id),
        'Authors':Authors.objects.all(),
        'Author':Books.objects.get(id=id).uploaded_by.all(),
    }
    return render(request,"book_info.html",context)