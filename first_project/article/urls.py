from django.urls import path, re_path,register_converter
from django.shortcuts import redirect, reverse
from article import views



app_name = "article"

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.article_login,name='login'),
    path('redir/', views.redir,name='redirect'),
    path('high/<id>/<name>/', views.article_highlight,name='high'),
    # re_path(r'.*list/(?P<categories>\w+|(\w+\+\w+)+)/', views.article_list, name='cate')
    path('list/<cate:categories>/', views.article_list, name='cate'),
]
