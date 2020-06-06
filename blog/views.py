from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import ArticleForm, CommentForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def getArticlesTitle(request):
   articles = Article.objects.all().values('title', 'created_at')
   return JsonResponse(list(articles), safe=False)


# Create your views here.
def index(request):
   # return HttpResponse('hello django world')
   return render(request, 'index.html')

def articles(request):
   keyword = request.GET.get('keyword')
   if keyword:
      articles = Article.objects.filter(title__icontains = keyword)
      return render(request, 'articles.html', {'articles': articles})

   articles = Article.objects.all() # return []
   return render(request, 'articles.html', {'articles': articles})


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
   comments = article.comment_list.all()
   # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-object-or-404
   return render(request, 'detail.html', {'article': article, 'comments': comments})


@login_required(login_url='user:login')
def addComment(request, article_id):
   article = get_object_or_404(Article, id=article_id)

   form = CommentForm(request.POST or None)
   if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.article = article
      comment.save()
   return redirect('blog:detail', id=article_id)



@login_required(login_url='user:login') 
def dashboard(request):
   articles = Article.objects.filter(author=request.user) # dict olarak geliyor
   # try to request.user.id
   return render(request, 'dashboard.html', {'articles': articles})


@login_required(login_url='user:login') 
def addArticle(request):
   form = ArticleForm(request.POST or None, request.FILES or None)
   if form.is_valid():
      # Create, but don't save the new article instance. commit=False
      article = form.save(commit=False)
      # Modify the article in some way.
      article.author = request.user
      # Save the new instance.
      article.save()
      
      messages.success(request, 'Article was successfully added')
      return redirect('blog:dashboard')
   return render(request, 'addArticle.html', {'form': form})


@login_required(login_url='user:login')
def updateArticle(request, id):
   article = get_object_or_404(Article, id=id)
   form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
   if form.is_valid():
      form.save()
      messages.success(request, 'Article was successfully updated')
      return redirect('blog:dashboard')
   return render(request, 'updateArticle.html', {'form': form})


@login_required(login_url='user:login')
def deleteArticle(request, id):
   article = get_object_or_404(Article, id=id)
   article.delete()
   mesage_with_title = 'Article was successfully deleted' + " ( " + article.title + ") "
   messages.success(request, mesage_with_title)
   return redirect('blog:dashboard')
   