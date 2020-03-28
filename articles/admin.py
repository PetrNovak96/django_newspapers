from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline): # este existuje StackedInline

    model = Comment

class ArticleAdmin(admin.ModelAdmin):

    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin) # new tady pozor, tady to taky musi byt
admin.site.register(Comment) # new