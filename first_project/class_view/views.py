from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.

def index(request):
    return HttpResponse("index")

class BookListView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("BookListView")
    def http_method_not_allowed(self, request,*args,**kwargs):
        return HttpResponse("不支持POST请求")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request, "class_addbook.html")
    def post(self,request,*args,**kwargs):
        book_name = request.POST.get("name")
        book_author = request.POST.get("author")
        print(f"{book_name} : {book_author}")
        return HttpResponse("success")

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self,**kwargs):
        context = {"phone":"85292047291"}
        return context