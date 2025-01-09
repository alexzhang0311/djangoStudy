from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "classview"
urlpatterns = [
    path("",views.index,name="index"),
    path("view/",views.BookListView.as_view(),name="bookview"),
    path("addview/",views.AddBookView.as_view(),name="addbookview"),
    #针对静态HTML页面，直接进行渲染
    # path("about/",TemplateView.as_view(template_name='about.html'))
    #传入上下文参数到html模板
    path("about/",views.AboutView.as_view())
]