from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("articles/<str:article_name>", views.view_article, name = 'view article'),
    path('about_us', views.about_page, name = 'about us'),
    path('articles', views.articles_page, name = 'articles page')
]   