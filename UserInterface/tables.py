import django_tables2 as tables 
from Models.models import Articles


class ArticlesTable(tables.Table):
    class Meta:
        template_name = "UserInterface/index.html"
        model = Articles
        fields = ['author', 'date_created', 'title']