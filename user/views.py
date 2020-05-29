from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


def register(request):
   form = RegistrationForm(request.POST or None)
   if form.is_valid(): # form.is_valid() metodu RegistrationForm daki clean() metodunu cagiriyor. yani trigger ediyor
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')

         new_user = User(username=username)
         new_user.set_password(password)
         new_user.save()
         login(request, new_user)
         return redirect('blog:index')
      
   context = {
      'form': form
   }
   return render(request, 'register.html', context)

   # another way
   # if request.method == "POST":
   #    form = RegistrationForm(request.POST)
   #    if form.is_valid(): # form.is_valid() metodu RegistrationForm daki clean() metodunu cagiriyor. yani trigger ediyor
   #       username = form.cleaned_data.get('username')
   #       password = form.cleaned_data.get('password')

   #       new_user = User(username=username)
   #       new_user.set_password(password)
   #       new_user.save()
   #       login(request, new_user)
   #       return redirect('blog:index')
      
   #    context = {
   #       'form': form
   #    }
   #    return render(request, 'register.html', context)

   # else:
   #    form = RegistrationForm()
   #    context = {
   #       'form': form
   #    }
   #    return render(request, 'register.html', context)

def loginUser(request):
   return render(request, 'login.html')

def logoutUser(request):
   pass