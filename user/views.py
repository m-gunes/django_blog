from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.


def register(request):
   
   form = RegistrationForm(request.POST or None)
   context = {
      'form': form
   }
   try:
      if form.is_valid(): # form.is_valid() metodu RegistrationForm daki clean() metodunu cagiriyor. yani trigger ediyor
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            messages.success(request, 'Kayit isleminiz basari ile gerceklesti.')
            return redirect('blog:index')
         
      return render(request, 'register.html', context)

   except IntegrityError as err:
      messages.error(request, err)
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