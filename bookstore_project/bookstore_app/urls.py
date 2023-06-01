from django.urls import path
from . import views
app_name = 'bookstore_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:book_id>/', views.details, name='details'),
    path('add/', views.add_books, name='add_books'),
    path('update/<int:book_id>/', views.update, name='update'),
    path('delete/<int:book_id>/', views.delete, name='delete')

]
