from django.shortcuts import render

# Create your views here.
data = {
    "username":"alexzhang"
}

def index(request):
    return render(request, "template_include.html",context=data)


def company(request):
    return render(request, "company.html")

def campus(request):
    return render(request, "campus.html")