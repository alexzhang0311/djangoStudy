from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


class Person(object):
    def __init__(self, name):
        self.name = name


p = Person("张弛")


def movie(request):
    # html = render_to_string("index.html")
    # return HttpResponse(html)
    data = {"username": "alexzhang",
            "person": p,
            "car": {"color": "red", "brand": "Benz"},
            "hobbies": ["basketball", "football"]
            }
    return render(request, 'index.html', context=data)


def movie_login(request):
    return HttpResponse("电影登录页")