from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic import DetailView
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout




# list all books in the database
def books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# display details of a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


# register
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

def logout(request):
    logout(request) 
    return redirect('home')


    