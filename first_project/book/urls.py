from django.urls import path
from book import views

app_name = "book"
urlpatterns = [
    path('', views.book),
    path('login/<book_id>', views.book_login, name='sso'),
    path('detail/<book_id>/', views.book_detail),
    path('author/', views.book_author),
    path('publish/<int:publish_id>/', views.book_publisher)
]