from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request, 'home.html')

def custom(request):
     return render(request, 'custom.html') 
   
def contact(request):
     return render(request, 'contact.html')

def about(request):
     return render(request, 'about.html')     

def search(request):
     return render(request, 'search.html')     

     