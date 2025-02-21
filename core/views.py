from django.shortcuts import render,redirect
from items.models import Category,Item
from .forms import SignupForm

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

def Signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            

            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            form = SignupForm()

        
        return render(request, 'core/signup.html',{
                'form': form
        })