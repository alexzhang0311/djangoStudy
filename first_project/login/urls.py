from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('submit_form/',views.submit_form,name="submit_form")
]

