from django.urls import path
from . import views

app_name = "jsonconvert"
urlpatterns = [
    path('', views.index,name="index"),
]