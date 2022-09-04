from django.shortcuts import render, HttpResponse, get_object_or_404
from Models.models import Events, Articles
from .tables import ArticlesTable
# Create your views here.

def index(request):
    list_articles = Articles.objects.all()
    items = {
        'articles': list_articles,
        'table': ArticlesTable(Articles.objects.all())
    }
    return render(request, "UserInterface/index.html", context =items )

def view_article(request, article_name):
    article = get_object_or_404(Articles, title = article_name)
    items = {
        'article': article
    }
    return render(request, 'UserInterface/view_article.html', context=items)


