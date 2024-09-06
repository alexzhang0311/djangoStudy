from django.urls import path
from . import views

app_name = "template_include"
urlpatterns = [
    path('',views.index,name="index"),
    path('company/',views.company,name="company"),
    path('campus/',views.campus,name="campus"),
]
