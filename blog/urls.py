from django.urls import path

from . import views

# https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names
# app_name is namespace
app_name = 'blog'

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('addArticle/', views.addArticle, name='addArticle'),
   path('article/<int:id>/', views.detail, name='detail'),
   path('update/<int:id>/', views.updateArticle, name='update'),
   path('delete/<int:id>', views.deleteArticle, name='delete')
]