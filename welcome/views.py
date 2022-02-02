from django.shortcuts import render, redirect
from .models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'welcome/index.html', {'home': index})


def catalog(request):
    books = Books.objects.all()
    return render(request, 'welcome/catalog.html', {'books': books})


def book_detail(request, id):
    selected_book = Books.objects.get(id = id)
    return render(request, 'welcome/book_detail.html', {'book_detail': selected_book})

#The function above is not working correctly. It shows us the book description of the first book in all the cards. BUT NOW WITH ID 3, 2 and 1 does not work anymore (I thinks it has to do with the books record)


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('catalog')
    else:
        form = UserCreationForm()
    return render(request, 'welcome/register.html', {'form': form})