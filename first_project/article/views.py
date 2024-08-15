from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse


def index(request):
    return HttpResponse("文章首页")


def article_list(request, categories):
    return HttpResponse("文章列表为:{}".format(categories))


def article_login(request):
    # text = reverse('article:cate',kwargs={"categories":"django+alex"})
    text = reverse('article:cate',kwargs={"categories":['django','alex']})
    return redirect(text)   