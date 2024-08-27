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
    context = {
        "books":[
            "水浒传",
            "三国演义",
            "红楼梦",
            "西游记",
            ],
        "persons":[
            {
            "name":"alexzhang",
            "gender":"Male",
            "age":"31"
            },
            {
            "name":"IrisYang",
            "gender":"Female",
            "age":"32"
            },
            {
            "name":"TimFeng",
            "gender":"Male",
            "age":"32"
            },
            {
            "name":"SihuiHa",
            "gender":"FeMale",
            "age":"32"
            }
        ]
    }
    return render(request, 'books.html', context=context)


def movie_login(request):
    return HttpResponse("电影登录页")

def movie_highlight(request, id):
    return HttpResponse("最热电影ID:{}".format(id))