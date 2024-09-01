from django.urls import include, path
from . import views

urlpatterns = [
    path('books', views.books, name='books'),
    path('books/library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # authenitcation
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]