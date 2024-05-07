from django.shortcuts import render, redirect
from .models import Category, Books
from .forms import BookForm

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'index.html', context=context)


def get_books(request, pk):
    books = Books.objects.filter(category=pk)
    context = {
        'books': books
    }
    return render(request, 'books.html', context=context)


def detail(request, pk):
    book = Books.objects.get(pk=pk)
    context = {
        'book':book
    }
    return render(request, 'detail.html',context=context)


def add_books(request):
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('get_info')
    context = {
        'form':form
    }
    return render(request,'create.html',context=context)


def update_books(request, pk):
    data = Books.objects.get(pk=pk)
    form = BookForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('get_info')
    context = {
        'form':form
    }
    return render(request, 'update.html',context=context)