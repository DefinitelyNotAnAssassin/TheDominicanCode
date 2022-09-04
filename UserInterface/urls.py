from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("articles/<str:article_name>", views.view_article, name = 'view article')
]