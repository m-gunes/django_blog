from django import forms
from .models import Article, Comment

# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
class ArticleForm(forms.ModelForm):
   class Meta:
      model = Article
      fields = ['title', 'content', 'image']



class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ['content']