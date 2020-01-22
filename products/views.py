from django.shortcuts import render

# Create your views here.

def get_products(req):
    return render(req,'add_product.html')