from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "template_include.html")


def company(request):
    return render(request, "company.html")

def campus(request):
    return render(request, "campus.html")