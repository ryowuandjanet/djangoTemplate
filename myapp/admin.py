from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class ArticleAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

admin.site.register(Article,ArticleAdmin)


