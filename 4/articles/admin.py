from django.contrib import admin
from django.db import models
from .models import Article,Comment

# Register your models here.

class CommentInLine(admin.StackedInline):
    model=Comment
    extra=0
class ArticleAdmin(admin.ModelAdmin):
    inlines=[

        CommentInLine,
    ]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)



