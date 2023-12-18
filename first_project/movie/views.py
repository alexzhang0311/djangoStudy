from django.shortcuts import render

from django.http import HttpResponse


def movie(request):
    return HttpResponse("电影首页")


def movie_login(request):
    return HttpResponse("电影登录页")