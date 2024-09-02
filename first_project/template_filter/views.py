from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    data = {
        "value1":[1,2,3],
        "value2":[4,5,6],
        "time":datetime.now(),
        "default":"hello",
        "default_0":[],
        "default_1":None,
        "floatValue":3.1415926
    }
    return render(request, "template_filter.html",context=data)