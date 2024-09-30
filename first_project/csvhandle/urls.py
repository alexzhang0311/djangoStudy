from django.urls import path
from . import views

app_name = "csvhandle"
urlpatterns = [
    path('', views.index,name="index"),
    path('stream/', views.stream_csv,name="stream"),
]