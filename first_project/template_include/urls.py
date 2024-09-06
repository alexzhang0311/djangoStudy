from django.urls import path
from . import views

app_name = "template_include"
urlpatterns = [
    path('',views.index,name="index"),
    path('company/',views.index,name="company"),
    path('campus/',views.index,name="campus"),
]
