from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagPosition, Tag


class TagPositionInlineFormset(BaseInlineFormSet):

    def clean(self):
        one_main = False
        for form in self.forms:
            try:
                print(form.cleaned_data['is_main'])
                if form.cleaned_data['is_main']:
                    if one_main:
                        raise ValidationError('Два главных тега')
                    else:
                        one_main = True
                else:
                    continue
            except KeyError:
                continue
        if not one_main:
            raise ValidationError('Нет главных тегов!')
        return super().clean()


class TagPositionInline(admin.TabularInline):
    model = TagPosition
    formset = TagPositionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [TagPositionInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']




