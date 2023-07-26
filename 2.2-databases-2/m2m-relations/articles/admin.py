from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import *

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            # В form.cleaned_data будет находиться словарь с данными
            # каждой отдельной формы, которые можно проверить
            if form.cleaned_data.get('is_main'):
                if is_main:
                    raise ValidationError('is_main уже есть')

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if not is_main:
            raise ValidationError('Нет is_main')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = BaseInlineFormSet

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
