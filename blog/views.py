from django.shortcuts import render
from django.http import HttpResponse

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
   return HttpResponse('Detail id is ' + str(id))
   
   