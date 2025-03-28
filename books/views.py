from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponseNotAllowed
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    books=Book.objects.all()
    context = {"books":books}
    return render(request, "index.html", context)
    # response=""
    # for book in books:
    #      response += f"{book.title} by {book.author}"
    # return HttpResponse(response)

@login_required
def create(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=BookForm()
        print(form)
    return render(request,'create.html',{'form':form})

@login_required
def edit_book(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method=="POST":
         form=BookForm(request.POST, instance=book)
         if form.is_valid():
             form.save()
             return redirect('index')
    else:
        form=BookForm(instance=book)
    return render(request,'create.html',{'form':form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":  
        book.delete()
        return redirect('index')
    
    return render(request,'index.html',{'book':book})  


# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     book.delete()
#     return redirect('index')

