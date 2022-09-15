
from symbol import factor
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db.models.functions import Lower
# Create your models here.

class OrganizationAccount(AbstractUser):
    OrgRole = [('President', 'President'),('Internal VP', 'Internal Vice President'), ('External VP', 'External Vice President'),
    ('Treasurer', 'Treasurer'), ('Secretary', 'Secretary'), 
    ("Assistant Secretary", "Assistant Secretary"), ("Auditor", "Auditor"), ("Outreach Program Director", "Outreach Program Director"), ("Event Coordinator", "Event Coordinator"),
    ("Public Information Officer", "Public Information Officer"), ("Digital Officer", "Digital Officer"), ("Representative", "Representative"), ('Member', 'Member')
    
    
    ]
    role = models.CharField(choices = OrgRole, max_length=32)
    image_link = models.CharField(max_length=555, default = "https://preview.redd.it/h5gnz1ji36o61.png?width=225&format=png&auto=webp&s=84379f8d3bbe593a2e863c438cd03e84c8a474fa")
    description = models.CharField(max_length=255, default="Description")
    facebook_link = models.CharField(max_length=555, default = "https://www.facebook.com")

    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return f'{self.first_name} | {self.role}'

class Articles(models.Model):
    author = models.ForeignKey(OrganizationAccount, on_delete=models.CASCADE)
    content = models.CharField(max_length=1250)
    date_created = models.DateTimeField()
    title = models.CharField(max_length=64, default="Untitled", unique=True)

    def __str__(self):
        return f'{self.author} / {self.title} '

class Events(models.Model):
    event_name = models.CharField(max_length=128)
    event_date = models.DateTimeField()

    def __str__(self):
        return f'{self.event_name} | {self.event_date}'


class RegisterList(models.Model):
    date = models.DateField(default=now)
    name = models.CharField(max_length=32)
    program = models.CharField(max_length=32)
    level = models.CharField(max_length=16)
    facebook_link = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name = 'name_unique'
            )
        ]
        unique_together = ('name', 'program', 'level')
        
    def __str__(self):
        return f"{self.date} / {self.name} / {self.program} - {self.level}"



