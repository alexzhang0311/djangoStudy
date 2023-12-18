from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect, reverse


def book_login(request):
    return HttpResponse("图书APP登录页")


def book(request):
    if request.GET.get("user") == 'alexzhang':
        return HttpResponse("您好:{}\r\n您目前访问的是图书首页".format(request.GET.get("user")))
    else:
        #return redirect('login/')
        # return redirect(reverse('book:sso'))
        current_namespace = request.resolver_match.namespace
        return redirect(reverse('{}:sso'.format(current_namespace)))


def book_detail(request, book_id):
    text = "图书ID是：{}".format(book_id)
    return HttpResponse(text)


def book_author(request):
    author_id = request.GET.get("id")
    text = "作者的ID是：{}".format(author_id)
    return HttpResponse(text)


def book_publisher(request, publish_id):
    text = "出版社ID是：%s" % publish_id
    return HttpResponse(text)
