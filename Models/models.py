from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class OrganizationAccount(AbstractUser):
    OrgRole = [('President', 'President'),('Internal VP', 'Internal Vice President'), ('External VP', 'External Vice President'),
    ('Treasurer', 'Treasurer'), ('Secretary', 'Secretary'), ('Member', 'Member')
    
    
    ]
    role = models.CharField(choices = OrgRole, max_length=32)
    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return f'{self.first_name} | {self.role}'

class Articles(models.Model):
    author = models.ForeignKey(OrganizationAccount, on_delete=models.CASCADE)
    content = models.CharField(max_length=1250)
    date_created = models.DateTimeField()
    title = models.CharField(max_length=64, default="Untitled")

    def __str__(self):
        return f'{self.author} / {self.title} '

class Events(models.Model):
    event_name = models.CharField(max_length=128)
    event_date = models.DateTimeField()




