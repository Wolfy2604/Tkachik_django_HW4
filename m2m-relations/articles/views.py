from django.shortcuts import render

from articles.models import Article, Tag, TagPosition


def articles_list(request):
    template = 'articles/news.html'
    context = {
        'context_article': Article.objects.order_by('-published_at'),
    }

    return render(request, template, context)
