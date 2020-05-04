from django.shortcuts import render
from django.views import View
from .models import News
from django.db.models import Q

class Index(View):
    def get(self, request):
        news = News.objects.all()
        search_key_word = request.GET.get('key-word')
        if search_key_word:
            news = news.filter(
                Q(title__icontains=search_key_word) | 
                Q(text__icontains=search_key_word))
        context = {
            'news' : news,
            'search_key_word' : search_key_word,            
        }
        return render(request, 'Lab1/index.html', context=context)
