from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,reverse
import json


def index(request):
    if request.method == "GET":
        return render(request, "jsonconvert.html",context={"title":"Json格式化"})
    else:
        text = request.POST.get("my-textbox")
        try:
            json_object = json.loads(text)
            print(json_object)
        except ValueError:
            return HttpResponse("非JSON格式数据")
        return HttpResponse(text,content_type='application/json;charset=utf-8')