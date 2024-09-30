from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.core.handlers.wsgi import WSGIRequest


def index(request):
    for key,value in request.META.items():
        print(key,value)
    
    print(request.COOKIES)
    print(request.method)
    return HttpResponse("文章首页")

def article_list(request, categories):
    return HttpResponse("文章列表为:{}".format(categories))

def article_list_bak(request, categories):
    return HttpResponse("文章列表为:{}".format(categories))

def article_highlight(request, id,name):
    return HttpResponse("最热文章ID:{}，文章名是:{}".format(id,name))

def article_login(request):
    # text = reverse('article:cate',kwargs={"categories":"django+alex"})
    text = reverse('article:cate',kwargs={"categories":['django','alex']}) 
    return redirect(text)   

def redir(request):
    dir = request.GET.get("next")
    print(dir)
    return redirect(dir)


# @require_http_methods(["GET"])
@require_GET
def get_http_methods(request):
    return HttpResponse("This is Get")

# @require_http_methods(["POST"])
@require_POST
def post_http_methods(request):
    content = request.POST.get("content")
    # content = request.body.decode('utf-8')
    print(content)
    return HttpResponse("This is Post")

@require_http_methods(["GET","POST"])
def post_get_methods(request):
    if request.method == 'GET':
        return HttpResponse("This is Get")
    else:
        return HttpResponse("This is POST")