from django.shortcuts import render
from items.models import Category,Item

# Create your views here.

def index(request): #request give info about if its a get or post, details about the browser , ip address
     items = Item.objects.filter(is_sold = False)[0:6]
     Categories = Category.objects.all()
     return render(request, 'core/index.html',{
             'categories' : Categories,
             'items' : items
     }) 

def contact(request):
          return render(request, 'core/contact.html')