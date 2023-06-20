from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Books
from . forms import BookForm

# Create your views here.
def index(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books': books})
def details(request, book_id):
    book = Books.objects.get(id=book_id)
    return render(request,'details.html', {'book': book})
def add_books(request):
    if request.method == 'POST':
        book_name = request.POST.get('name')
        desc = request.POST.get('description')
        price = request.POST.get('price')
        img = request.FILES['image']
        books = Books(book_name=book_name,description=desc,price=price,image=img)
        books.save()
        return redirect('/')
    return render(request, 'add.html')
def update(request,book_id):
    book = Books.objects.get(id=book_id)
    form = BookForm(request.POST or None, request.FILES, instance= book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book':book})
def delete(request,book_id):
    if request.method == 'POST':
        book = Books.objects.get(id=book_id)
        book.delete()
        return redirect('/')
    return render(request, 'delete.html')
