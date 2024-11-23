from django.contrib import admin

from .models import Articles, Comments, ArticleReaction

admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(ArticleReaction)