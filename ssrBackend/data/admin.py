from django.contrib import admin

# Register your models here.

from .models import Project,teamDetails

admin.site.register(Project)
admin.site.register(teamDetails)