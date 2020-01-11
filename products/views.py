from django.shortcuts import render,redirect
from .models import Product
from django.core.files.storage import FileSystemStorage

# Create your views here.

def get_products(req):
    return render(req,'add_product.html')

def post_add_product(req):
    product_name=req.POST['product_name']
    product_price=req.POST['product_price']
    product_model=req.POST['product_model']
    product_category=req.POST['product_category']
    product_gender=req.POST['product_gender']
    product_details=req.POST['product_details']

    product_pic=req.FILES['product_pic']

    fs=FileSystemStorage()
    filename=fs.save(product_pic.name,product_pic)

    url=fs.url(filename)

    product=Product(product_pic=url,product_name=product_name,product_price=product_price,product_model=product_model,product_category=product_category,product_gender=product_gender,product_details=product_details)
    product.save()

    return redirect('home')