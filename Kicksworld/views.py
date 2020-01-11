from django.shortcuts import render
from products.models import Product
# Create your views here.

def home(request):
     all_products=Product.objects.all()
     context={
          "products":all_products
     }
     return render(request, 'home.html',context=context)

def custom(request):
     return render(request, 'custom.html') 
   
def contact(request):
     return render(request, 'contact.html')

def about(request):
     return render(request, 'about.html')     

def search(request):
     return render(request, 'search.html')     

     