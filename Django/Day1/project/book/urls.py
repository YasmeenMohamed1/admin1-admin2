from django.urls import path , include
from .views import *

urlpatterns = [

    path('list' , list_books , name = 'list_books'),
    path('details/<str:name>' , details_of_books , name = 'details_of_books'),
    path('update/<id>' , update_book , name = 'update_book'),
    path('delete/<int:id>' , delete_book , name = 'delete_book'),

]