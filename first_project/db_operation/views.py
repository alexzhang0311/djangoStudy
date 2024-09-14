from django.shortcuts import render,redirect,reverse
from django.db import connection
from django.http import HttpResponse

def get_cursor():
    return connection.cursor()

# Create your views here.
def index(request):
    cursor = get_cursor()
    cursor.execute("select id,title,author from book")
    books = cursor.fetchall()
    return render(request, 'db_index.html',context={"books":books})


def add_book(request):
    if request.method == "GET":
        return render(request, 'db_addbook.html')
    else:
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute(f"insert into book(title,author) values ('{bookname}','{author}')")
        print(bookname,author)
        return redirect(reverse("db:index"))


def book_detail(request,bookid):
    cursor = get_cursor()
    cursor.execute(f"select id,title,author from book where id = {bookid}")
    books = cursor.fetchone()
    return render(request, 'db_bookdetail.html',context={"books":books})

def book_delete(request):
    if request.method == "POST":
        bookid = request.POST.get('bookid')
        cursor = get_cursor()
        cursor.execute(f"delete from book where id = {bookid}")
        return redirect(reverse("db:index"))
    else:
        return HttpResponse("Invalid request method.")

def book_change(request):
    if request.method == "POST":
        bookid = request.POST.get('bookid')
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute(f"update book set title='{bookname}',author='{author}' where id={bookid}")
        return redirect(reverse("db:index"))
    else:
        return HttpResponse("Invalid request method.")