from django.urls import path, re_path,register_converter
from django.shortcuts import redirect, reverse
from article import views



app_name = "article"

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.article_login,name='login'),
    path('redir/', views.redir,name='redirect'),
    path('high/<id>/<name>/', views.article_highlight,name='high'),
    path('get/', views.get_http_methods,name='get'),
    path('post/', views.post_http_methods,name='post'),
    path('postget/', views.post_get_methods,name='postget'),
    # re_path(r'.*list/(?P<categories>\w+|(\w+\+\w+)+)/', views.article_list, name='cate')
    path('list/<cate:categories>/', views.article_list, name='cate'),
]
