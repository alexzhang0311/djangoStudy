from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse


# Create your views here.


def login(request):
    dir = request.GET.get("next")
    data = {
        "next":dir
    }
    return render(request, 'login.html',context=data)
    # return HttpResponse("欢迎访问登录页面，您的重定向页面是:{}".format(dir))


def index(request):
    token = request.GET.get("token")
    if token:
        return HttpResponse(f"{token}你好，欢迎访问登录首页")
    else:
        url = reverse('login:login') + "?next={}".format(reverse('login:index'))
        return redirect(url)


def submit_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        token = username
        nexturl = request.POST.get('next')
        url = nexturl + "?token={}".format(token)
        return redirect(url)
        # return HttpResponse(f"Received username: {username} and password: {password}")
    else:
        return HttpResponse("Invalid request method.")
