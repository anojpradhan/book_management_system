from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.index, name="index"),
    path('create',views.create,name='create'),
    path('edit/<int:book_id>/',views.edit_book,name="edit"),
    path('delete/<int:book_id>/',views.delete_book,name="delete"),
]