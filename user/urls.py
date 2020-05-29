from django.urls import path

from . import views

# https://docs.djangoproject.com/en/3.0/intro/tutorial03/#namespacing-url-names
# app_name is namespace
app_name = 'user'

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.loginUser, name='login'),
   path('logout/', views.logoutUser, name='logout'),
]