from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
   list_display = ['title', 'author', 'created_at']
   list_display_links = ['title', 'created_at']
   search_fields = ['title']
   list_filter = ['created_at']

admin.site.register(Article, ArticleAdmin)

# another way 
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#    list_display = ['author', 'title']
#    class Meta:
#       model = Article
