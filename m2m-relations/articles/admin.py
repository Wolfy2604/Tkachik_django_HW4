from django.contrib import admin

from .models import Article, TagPosition, Tag


class TagPositionInline(admin.TabularInline):
    model = TagPosition


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [TagPositionInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']




