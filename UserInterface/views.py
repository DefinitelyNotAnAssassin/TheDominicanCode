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


def about_page(request):
    return render(request, 'UserInterface/about_us.html')


def articles_page(request):
    article = Articles.objects.all().order_by('-date_created')
    print(article)
    items = {
        'articles': article

    }
    return render(request, 'UserInterface/articles.html', context = items)

