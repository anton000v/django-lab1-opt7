from django.contrib import admin
from . import models

class NewsAdmin(admin.ModelAdmin):
    class Meta:
        model = models.News

admin.site.register(models.News, NewsAdmin)


