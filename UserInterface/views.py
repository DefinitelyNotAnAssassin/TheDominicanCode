from django.shortcuts import render, HttpResponse, get_object_or_404
from Models.models import Events, Articles, OrganizationAccount
from .tables import ArticlesTable
from .form import RegisterForm

# Create your views here.

def index(request):
    list_articles = Articles.objects.all()
    items = {
        'articles': list_articles,
        'table': ArticlesTable(Articles.objects.all().order_by('-date_created'))
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
    
    items = {
        'table' : ArticlesTable(data = article)

    }
    return render(request, 'UserInterface/articles.html', context = items)

def register_page(request):

    if request.method == "GET":
        items = {
            'form': RegisterForm()
        }
        return render(request, 'UserInterface/register.html', context = items)

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponse("An organization representative would contact you soon.")
        else:
            items = {
                'form' : form
            }
            return render(request,'UserInterface/error.html',context = items)

    else:
        return HttpResponse("Invalid Request Method. Bad HTTP Header.")


def contact_us(request):
    org_members = OrganizationAccount.objects.all()
    items = {
        'members': org_members
    }
    return render(request, 'UserInterface/contact_us.html', context = items)