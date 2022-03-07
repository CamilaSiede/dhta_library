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

#API VIEWS 

@api_view(['GET','POST'])
def api_book_list(request):

    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        desserializer = BookSerializer(data=request.data)
        if desserializer.is_valid(): 
            desserializer.save() 
            return Response(desserializer.data, status=status.HTTP_201_CREATED)
        return Response(desserializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
def api_student_detail(request, pk):
    try:                                        # In the try/except block we are checking if the student with that ID exists.
        student = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(student, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
