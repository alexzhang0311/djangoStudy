from django.urls import path
from . import views

app_name = "uploadfile"
urlpatterns = [
    path('', views.index,name="index"),
    path('upload/', views.uploadfile,name="upload"),
    path('display/', views.displayfile,name="display"),
    path('content/', views.filedetail,name="content")
    ]