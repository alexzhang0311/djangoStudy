from django.urls import path
from . import views

app_name = "template_filter"
urlpatterns = [
    path('',views.index,name="index")
]