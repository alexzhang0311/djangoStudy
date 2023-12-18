from django.urls import path
from movie import views

#APP应用命名空间
app_name = "movie"

urlpatterns = [
    path('', views.movie),
    path('login/', views.movie_login, name='sso')
]
