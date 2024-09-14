from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection,transaction
import json

# Create your views here.
def get_cursor():
    return connection.cursor()

def add_file(filename):
    cursor = get_cursor()
    sql = f"insert into file(filename) values('{filename}')"
    cursor.execute(sql)
    return "success"


def index(request):
    return render(request, "uploadfile_index.html")

def uploadfile(request):
    if request.method == "POST":
        myfile = request.FILES.get('myfile')
        with open(f"./files/{myfile.name}",'wb') as fp:
            for chunk in myfile.chunks():
                fp.write(chunk)
        add_file(myfile)
        return HttpResponse("upload success!")
    else:
        return render(request, "uploadfile.html")



def displayfile(request):
    cursor = get_cursor()
    sql = f"select * from file"
    cursor.execute(sql)
    files = cursor.fetchall()
    return render(request, 'filecontent.html',context={"files":files})



def filedetail(request):
    filename = request.POST.get('uploadfile')
    with open(f"./files/{filename}",'r',encoding='utf-8') as f:
        data = f.read()
    return render(request, "filedetail.html", context={"data":data})