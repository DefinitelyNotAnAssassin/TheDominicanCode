from django.contrib import admin
from . import models 


admin.site.register(models.OrganizationAccount)
admin.site.register(models.Events)
admin.site.register(models.Articles)


# Register your models here.
