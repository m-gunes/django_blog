from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
from django.contrib import messages



# Create your views here.
def index(request):
   # return HttpResponse('hello django world')
   return render(request, 'index.html')


def about(request):
   context = {
      'name': 'about',
      'explain': 'This is a project which experimental',
      'list': ['I am happy for you', "I have't see you for a while", "I have been very busy with my new job", "long time no see"]
   }
   return render(request, 'about.html', context)

def detail(request, id):
   # article = Article.objects.filter(id=id).first()
   # article = Article.objects.get(id=id)
   article = get_object_or_404(Article, id=id)
   # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-object-or-404
   return render(request, 'detail.html', {'article': article})


def dashboard(request):
   articles = Article.objects.filter(author=request.user) # dict olarak geliyor
   # try to request.user.id
   return render(request, 'dashboard.html', {'articles': articles})
   
def addArticle(request):
   form = ArticleForm(request.POST or None)
   if form.is_valid():
      # Create, but don't save the new article instance. commit=False
      article = form.save(commit=False)
      # Modify the article in some way.
      article.author = request.user
      # Save the new instance.
      article.save()
      
      messages.success(request, 'Article was successfully added')
      return redirect('blog:index')

   return render(request, 'addArticle.html', {'form': form})