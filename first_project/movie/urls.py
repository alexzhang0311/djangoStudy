from django.urls import path
from movie import views

#APP应用命名空间
app_name = "movie"

urlpatterns = [
    path('', views.movie,name='index'),
    path('login/', views.movie_login, name='sso'),
    path('high/<id>/', views.movie_highlight, name='high')
]
