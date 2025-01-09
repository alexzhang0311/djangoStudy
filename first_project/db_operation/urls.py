from django.urls import path
from . import views

app_name = "db"
urlpatterns = [
    path('', views.index,name="index"),
    path('addbook/', views.add_book,name="addbook"),
    path('bookdetail/<int:bookid>', views.book_detail,name="bookdetail"),
    path('bookdelete/', views.book_delete,name="bookdelete"),
    path('bookupdate/', views.book_change,name="bookupdate"),
    path('orm/addbook/', views.ormBook,name="ormBook")
]