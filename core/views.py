from django.shortcuts import render

# Create your views here.

def index(request): #request give info about if its a get or post, details about the browser , ip address
     return render(request, 'core/index.html')

def contact(request):
          return render(request, 'core/contact.html')