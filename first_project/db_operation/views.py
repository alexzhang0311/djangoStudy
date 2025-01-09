from django.shortcuts import render,redirect,reverse
from django.db import connection
from django.http import HttpResponse
from .models import OrmBook

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

def ormBook(request):
    ###数据添加###
    # book = OrmBook(name="三国演义",author="罗贯中",price="100")
    # book = OrmBook(name="西游记",author="吴承恩",price="200")
    # book.save()
    # return HttpResponse("数据添加成功")
    ###数据查询###
    # book = OrmBook.objects.get(pk=1)
    # book = OrmBook.objects.filter(name="西游记")[0]
    # print(book)
    # return HttpResponse(book)

    ###数据删除###
    # book = OrmBook.objects.get(pk=1)
    # book.delete()
    # return HttpResponse("数据删除成功")

    ###数据修改
    book = OrmBook.objects.filter(author="吴承恩")[0]
    book.price = 100
    book.save()
    return HttpResponse("数据修改成功")