"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path,converters
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

def index(request):
    return render(request, "first_project.html",context={"title":"Django学习导航"})


def blackhole(request):
    return HttpResponse("黑洞吸收一切")


def relist(request, year):
    return HttpResponse("%s" % year)


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
    #同一个APP下有两个实例，通过命名空间来进行区分
    path('book1/', include('book.urls', namespace='book1')),
    path('book2/', include('book.urls', namespace='book2')),
    path('article/', include('article.urls')),
    path('login/',include('login.urls')),
    path('template/',include('template_filter.urls')),
    path('template_include/',include('template_include.urls')),
    path('template_static/',include('template_static.urls')),
    path('db/',include('db_operation.urls')),
    path('uploadfile/',include('uploadfile.urls')),
    path('json/',include('jsonconvert.urls')),
    path('csv/',include('csvhandle.urls')),
    path('classview/',include('class_view.urls')),
    path('accounts/', include('accounts.urls')),
    re_path(r"^list/(?P<year>\d{4})/$", relist),
    re_path(r'.*', blackhole)
    
]
