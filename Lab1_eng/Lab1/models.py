from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.CharField(max_length=700, verbose_name='Текст')
    # created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def clean(self):
        self.published_date = timezone.now()
        # self.save()

    def __str__(self):
        return self.title